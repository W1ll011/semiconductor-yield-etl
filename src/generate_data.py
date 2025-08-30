import os
import uuid
import numpy as np
import pandas as pd

BASE    = os.path.dirname(__file__)
RAW_DIR = os.path.join(BASE, "..", "data", "raw")
os.makedirs(RAW_DIR, exist_ok=True)

def simulate_lot(lot_id, wafers=25, dies_per_wafer=100):
    records = []
    for w in range(1, wafers + 1):
        rate = np.random.uniform(0.05, 0.20)
        for d in range(1, dies_per_wafer + 1):
            result = np.random.choice(["PASS", "FAIL"], p=[1-rate, rate])
            records.append({
                "lot_id":      lot_id,
                "wafer_id":    w,
                "die_id":      d,
                "test_result": result
            })
    return pd.DataFrame(records)

def main(num_lots=1000):
    all_frames = []
    for _ in range(num_lots):
        lid = uuid.uuid4().hex[:8]
        df  = simulate_lot(lid)
        all_frames.append(df)

    combined = pd.concat(all_frames, ignore_index=True)
    out_path = os.path.join(RAW_DIR, "all_lots.csv")
    combined.to_csv(out_path, index=False)
    print(f"Written {combined.shape[0]} rows to {out_path}")

if __name__ == "__main__":
    main()