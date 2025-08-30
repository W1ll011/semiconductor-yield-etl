import os
import pandas as pd

BASE     = os.path.dirname(__file__)
RAW_DIR  = os.path.join(BASE, "..", "data", "raw")
PROC_DIR = os.path.join(BASE, "..", "data", "processed")
os.makedirs(PROC_DIR, exist_ok=True)

def load_raw():
    """
    Load the combined CSV of all lots.
    Expects a file named 'all_lots.csv' in RAW_DIR.
    """
    path = os.path.join(RAW_DIR, "all_lots.csv")
    return pd.read_csv(path)

def compute_yield(df):
    total = (
        df
        .groupby("lot_id")["die_id"]
        .count()
        .rename("gross_die")
    )
    good = (
        df[df.test_result == "PASS"]
        .groupby("lot_id")["die_id"]
        .count()
        .rename("good_die")
    )
    summary = pd.concat([total, good], axis=1).fillna(0)
    summary["yield"] = summary.good_die / summary.gross_die
    return summary.reset_index()

def main():
    df      = load_raw()
    summary = compute_yield(df)
    out     = os.path.join(PROC_DIR, "yield_summary.csv")
    summary.to_csv(out, index=False)
    print("Saved summary to", out)

if __name__ == "__main__":
    main()