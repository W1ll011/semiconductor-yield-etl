import os, uuid
import numpy as np
import pandas as pd

BASE = os.path.dirname(__file__)
RAW_DIR = os.path.join(BASE, "..", "data", "raw")
os.makedirs(RAW_DIR, exist_ok=True)

def simulate_lot(lot_id, wafers=25, dies_per_wafer=100):
    records = []
    for w in range(1, wafers + 1):
        rate = np.random.uniform(0.01, 0.05)  # 1–5% defect
        for d in range(1, dies_per_wafer + 1):
            result = np.random.choice(["PASS", "FAIL"], p=[1 - rate, rate])
            records.append({
                "lot_id": lot_id,
                "wafer_id": w,
                "die_id": d,
                "test_result": result
            })
    return pd.DataFrame(records)

def main(num_lots=5):
    for _ in range(num_lots):
        lid = uuid.uuid4().hex[:8]
        df = simulate_lot(lid)
        path = os.path.join(RAW_DIR, f"lot_{lid}.csv")
        df.to_csv(path, index=False)
        print("Generated", path)

if __name__ == "__main__":
    main()