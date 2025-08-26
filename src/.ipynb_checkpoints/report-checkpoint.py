import os
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
PROC_DIR = os.path.join(BASE_DIR, "..", "data", "processed")
REPORT_DIR = os.path.join(BASE_DIR, "..", "reports")
os.makedirs(REPORT_DIR, exist_ok=True)

def load_summary():
    path = os.path.join(PROC_DIR, "yield_summary.csv")
    return pd.read_csv(path)

def export_excel(df):
    out_path = os.path.join(REPORT_DIR, "yield_report.xlsx")
    writer = pd.ExcelWriter(out_path, engine="xlsxwriter")
    df.to_excel(writer, index=False, sheet_name="Yield Summary")

    # Apply formatting
    workbook  = writer.book
    worksheet = writer.sheets["Yield Summary"]

    # Format header
    header_format = workbook.add_format({
        "bold": True,
        "bg_color": "#DCE6F1",
        "border": 1,
        "align": "center"
    })

    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)

    # Format yield column as percentage
    yield_col_index = df.columns.get_loc("yield")
    percent_format = workbook.add_format({"num_format": "0.00%", "border": 1})
    worksheet.set_column(yield_col_index, yield_col_index, 12, percent_format)

    # Auto-fit other columns
    for i, col in enumerate(df.columns):
        max_len = max(df[col].astype(str).map(len).max(), len(col)) + 2
        worksheet.set_column(i, i, max_len)

    writer.close()
    print(f"Excel report saved to {out_path}")

def main():
    df = load_summary()
    export_excel(df)

if __name__ == "__main__":
    main()