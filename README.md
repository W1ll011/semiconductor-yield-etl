# Semiconductor Yield ETL

A reproducible pipeline for generating, processing, and reporting semiconductor wafer yield data. Includes modular Python scripts, Jupyter notebooks for exploration, and styled Excel output for easy sharing.

## Badges

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

---

## Installation (Windows Command Prompt)

```cmd
REM 1. Clone the repo
git clone git@github.com:YourUser/semiconductor-yield-etl.git
cd semiconductor-yield-etl

REM 2. Create a virtual environment
python -m venv .venv

REM 3. Activate the virtual environment
.\.venv\Scripts\activate

REM 4. Install dependencies
pip install -r requirements.txt

REM 5. (Optional) Launch JupyterLab
jupyter lab
```

---

## Project Structure

```
semiconductor-yield-etl/
├── .venv/                     # Virtual environment
├── data/
│   ├── raw/                   # Generated raw lot CSVs
│   └── processed/             # Yield summary CSV
├── notebooks/                 # Analysis and demo notebooks
├── reports/                   # Generated Excel reports
├── src/
│   ├── generate_data.py       # Synthesizes raw lot data
│   ├── etl.py                 # Computes yield summary
│   └── report.py              # Exports styled Excel report
├── requirements.txt           # Python dependencies
├── README.md                  # Project overview (this file)
└── .gitignore                 # Files and folders to ignore in Git
```

---

## Usage

In Windows Command Prompt, with the virtual environment activated:

```cmd
REM Generate raw data files
python src\generate_data.py

REM Compute the yield summary
python src\etl.py

REM Export the styled Excel report
python src\report.py
```

To preview the report in a notebook:

```cmd
jupyter lab
```

Then, within a notebook cell:

```python
import pandas as pd
df = pd.read_excel("../reports/yield_report.xlsx")
df.head()
```

---

## Features

- Synthesizes realistic lot-by-lot data for testing workflows
- Modular ETL scripts with clear input/output contracts
- Jupyter notebooks for step-by-step exploration and visualization
- Styled Excel reports via XlsxWriter, ready for stakeholders
- Windows-friendly setup and minimal system dependencies

---

## Contributing

- Fork the repository and create feature branches (feature/…)
- Commit often with descriptive messages
- Open pull requests against the main branch
- Update requirements.txt if you add new Python packages
- Run code linting and notebook checks before submitting

---

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.
