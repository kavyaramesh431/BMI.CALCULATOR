# BMI Calculator (Python)

This project contains two interfaces for calculating and tracking Body Mass Index (BMI):
1. **Command-line (CLI)**: `cli.py` - simple prompts for weight and height, calculates BMI, shows category, and can save the result to the local database.
2. **Graphical (GUI)**: `main.py` - Tkinter-based GUI with inputs, result display, saving to database, history table, and BMI trend plotting (matplotlib).

## Features
- Input validation for weight (kg) and height (m or cm).
- Correct BMI calculation: BMI = weight_kg / (height_m ** 2)
- BMI categorization (Underweight, Normal, Overweight, Obese) based on WHO ranges.
- SQLite storage of records with timestamp.
- History viewing and plotting BMI over time in the GUI.

## Setup
1. (Optional) Create a virtual environment and activate it.
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\\Scripts\\activate  # Windows
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
   *Note:* Tkinter is part of the Python standard library on many systems. If your OS lacks it, install the system package (e.g., `sudo apt install python3-tk` on Debian/Ubuntu).
3. Run the GUI:
   ```bash
   python main.py
   ```
   Or run the CLI:
   ```bash
   python cli.py
   ```

## File overview
- `bmi_core.py` : BMI calculation + categorization utilities.
- `db.py`       : SQLite helpers for storing and retrieving BMI records.
- `cli.py`      : Command-line interface.
- `main.py`     : Tkinter GUI application (entry point).
- `requirements.txt`, `README.md`, `LICENSE`

## Notes & Next steps
- You can extend categories, export history to CSV, or add user profiles for multiple users.
- For natural-language input parsing (e.g., "I weigh 70 kg"), consider adding simple parsing logic or a small NLP model.

