# main.py - Tkinter GUI for BMI Calculator with history and plot
import tkinter as tk
from tkinter import ttk, messagebox
from bmi_core import calculate_bmi, categorize_bmi
import db
from datetime import datetime
import matplotlib
matplotlib.use('Agg')  # prevent trying to open a GUI backend during file creation; app uses FigureCanvas when run by user
from matplotlib.figure import Figure
try:
    # Importing canvas for use when the app runs normally
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
except Exception:
    FigureCanvasTkAgg = None

class BMIGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('BMI Calculator')
        self.geometry('700x500')
        self.create_widgets()
        db.init_db()
        self.refresh_history()

    def create_widgets(self):
        frm = ttk.Frame(self, padding=10)
        frm.pack(fill='x', expand=False)

        ttk.Label(frm, text='Weight (kg):').grid(column=0, row=0, sticky='w')
        self.weight_var = tk.StringVar()
        ttk.Entry(frm, textvariable=self.weight_var).grid(column=1, row=0, sticky='w')

        ttk.Label(frm, text='Height (m or cm):').grid(column=0, row=1, sticky='w')
        self.height_var = tk.StringVar()
        ttk.Entry(frm, textvariable=self.height_var).grid(column=1, row=1, sticky='w')

        calc_btn = ttk.Button(frm, text='Calculate', command=self.on_calculate)
        calc_btn.grid(column=0, row=2, pady=8)

        save_btn = ttk.Button(frm, text='Save', command=self.on_save)
        save_btn.grid(column=1, row=2, pady=8)

        plot_btn = ttk.Button(frm, text='Plot History', command=self.on_plot)
        plot_btn.grid(column=2, row=2, pady=8)

        # Result display
        self.result_var = tk.StringVar(value='BMI: -  Category: -')
        ttk.Label(self, textvariable=self.result_var, font=('Helvetica', 12, 'bold')).pack(pady=6)

        # History table
        cols = ('id', 'weight', 'height', 'bmi', 'category', 'timestamp')
        self.tree = ttk.Treeview(self, columns=cols, show='headings', height=10)
        for c in cols:
            self.tree.heading(c, text=c.title())
            self.tree.column(c, width=100)
        self.tree.pack(fill='both', expand=True, padx=10, pady=10)

    def parse_height(self, s):
        s = s.strip().lower()
        if not s:
            return None
        try:
            if s.endswith('cm'):
                return float(s[:-2].strip()) / 100.0
            if s.endswith('m'):
                return float(s[:-1].strip())
            val = float(s)
            if val > 3:
                return val / 100.0
            return val
        except:
            return None

    def on_calculate(self):
        try:
            weight = float(self.weight_var.get().strip())
            height = self.parse_height(self.height_var.get())
            if height is None or height <= 0:
                messagebox.showerror('Invalid input', 'Please enter a valid height (m or cm).')
                return
            bmi = calculate_bmi(weight, height)
            cat = categorize_bmi(bmi)
            self.current = (weight, height, bmi, cat)
            self.result_var.set(f'BMI: {bmi}  Category: {cat}')
        except Exception as e:
            messagebox.showerror('Error', f'Invalid input: {e}')

    def on_save(self):
        if not hasattr(self, 'current'):
            messagebox.showinfo('Save', 'No calculated BMI to save.')
            return
        weight, height, bmi, cat = self.current
        db.add_record(weight, height, bmi, cat, datetime.now().isoformat(sep=' ', timespec='seconds'))
        messagebox.showinfo('Saved', 'Record saved to history.')
        self.refresh_history()

    def refresh_history(self):
        for r in self.tree.get_children():
            self.tree.delete(r)
        rows = db.get_all_records()
        for row in rows:
            self.tree.insert('', 'end', values=row)

    def on_plot(self):
        rows = db.get_all_records()
        if not rows:
            messagebox.showinfo('Plot', 'No records to plot.')
            return
        timestamps = [r[5] for r in rows]
        bmis = [r[3] for r in rows]
        # Create figure
        fig = Figure(figsize=(6,3))
        ax = fig.add_subplot(111)
        ax.plot(bmis)
        ax.set_title('BMI over time')
        ax.set_xlabel('Record #')
        ax.set_ylabel('BMI')
        # show in a new tkinter window if canvas is available
        if FigureCanvasTkAgg is None:
            # Fallback: save the plot to a file and inform user
            fname = 'bmi_plot.png'
            fig.savefig(fname)
            messagebox.showinfo('Plot saved', f'Plot saved to {fname} in the current directory.')
        else:
            win = tk.Toplevel(self)
            win.title('BMI Plot')
            canvas = FigureCanvasTkAgg(fig, master=win)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True)

if __name__ == '__main__':
    app = BMIGUI()
    app.mainloop()
