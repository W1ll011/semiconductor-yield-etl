import os
import pandas as pd

BASE_DIR   = os.path.dirname(__file__)
RAW_DIR    = os.path.join(BASE_DIR, "..", "data", "raw")
REPORT_DIR = os.path.join(BASE_DIR, "..", "reports")
os.makedirs(REPORT_DIR, exist_ok=True)


def load_and_summarize():
    """
    1) Load the single 'all_lots.csv' file produced by the
       in-memory concatenation approach.
    2) Compute per-lot gross_die, good_die, and yield.
    """
    path = os.path.join(RAW_DIR, "all_lots.csv")
    df   = pd.read_csv(path)

    # total dies per lot
    total = (
        df
        .groupby("lot_id")["die_id"]
        .count()
        .rename("gross_die")
    )

    # passing dies per lot
    good = (
        df[df.test_result == "PASS"]
        .groupby("lot_id")["die_id"]
        .count()
        .rename("good_die")
    )

    summary = pd.concat([total, good], axis=1).fillna(0)
    summary["yield"] = summary.good_die / summary.gross_die

    return summary.reset_index()


def export_excel(df: pd.DataFrame):
    """
    Write out a formatted Excel report with one sheet:
    'Yield Summary'.
    """
    out_path = os.path.join(REPORT_DIR, "yield_report.xlsx")

    with pd.ExcelWriter(out_path, engine="xlsxwriter") as writer:
        df.to_excel(
            writer,
            index=False,
            sheet_name="Yield Summary"
        )

        workbook  = writer.book
        worksheet = writer.sheets["Yield Summary"]

        # --- Header formatting ---
        hdr_fmt = workbook.add_format({
            "bold":     True,
            "bg_color": "#DCE6F1",
            "border":   1,
            "align":    "center"
        })
        for col_idx, col_name in enumerate(df.columns):
            worksheet.write(0, col_idx, col_name, hdr_fmt)

        # --- Yield column as % ---
        ycol = df.columns.get_loc("yield")
        pct_fmt = workbook.add_format({
            "num_format": "0.00%",
            "border":     1
        })
        # set width + formatting on the yield column
        worksheet.set_column(ycol, ycol, 12, pct_fmt)

        # --- Auto-fit all other columns ---
        for idx, col in enumerate(df.columns):
            max_len = max(
                df[col].astype(str).map(len).max(),
                len(col)
            ) + 2
            worksheet.set_column(idx, idx, max_len)

    print(f"Excel report saved to {out_path}")


def main():
    summary = load_and_summarize()
    export_excel(summary)


if __name__ == "__main__":
    main()