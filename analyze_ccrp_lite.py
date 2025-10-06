import json
from pathlib import Path
from statistics import mean
import math

DATA_PATH = Path("ccrp_lite_dataset_v0_1.json")

def pearson(xs, ys):
    if len(xs) < 2: 
        return float("nan")
    mx, my = mean(xs), mean(ys)
    num = sum((x-mx)*(y-my) for x,y in zip(xs, ys))
    denx = math.sqrt(sum((x-mx)**2 for x in xs))
    deny = math.sqrt(sum((y-my)**2 for y in ys))
    return num / (denx*deny) if denx*deny != 0 else float("nan")

def main():
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    print("=== CCRP-Lite Dataset Analysis ===\n")
    print(f"Items: {len(data)}\n")

    # Per-item summary
    print("ID   | Entropy | FidelityGain | Context")
    print("-----+---------+--------------+-------------------------")
    entropies, gains = [], []
    for row in data:
        e = float(row["entropy_score"])
        g = float(row["fidelity_gain"])
        entropies.append(e); gains.append(g)
        ctx = row["context"][:25]
        print(f"{row['id']:<4} | {e:>7.2f} | {g:>12.2f} | {ctx}")

    # Aggregates
    avg_e = mean(entropies)
    avg_g = mean(gains)
    r = pearson(entropies, gains)

    print("\n--- Aggregates ---")
    print(f"Average Entropy Score     : {avg_e:.3f}")
    print(f"Average Fidelity Gain     : {avg_g:.3f}")
    print(f"Pearson r (Entropy ~ Gain): {r:.3f}")

    # Simple interpretation
    print("\n--- Interpretation ---")
    if r > 0.2:
        print("Higher collapse intensity tends to coincide with higher rebuild gain in this sample.")
    elif r < -0.2:
        print("Higher collapse intensity tends to coincide with lower rebuild gain in this sample.")
    else:
        print("Little linear relationship between collapse intensity and rebuild gain in this small sample.")

    # Buckets (optional quick view)
    print("\n--- Buckets ---")
    def bucket(e):
        if e >= 0.85: return "HIGH"
        if e >= 0.70: return "MID"
        return "LOW"
    buckets = {"HIGH": [], "MID": [], "LOW": []}
    for row in data:
        buckets[bucket(row["entropy_score"])].append(row["fidelity_gain"])
    for b, vals in buckets.items():
        if vals:
            print(f"{b:>4} entropy: n={len(vals)}, avg fidelity gain={mean(vals):.2f}")
        else:
            print(f"{b:>4} entropy: n=0")

if __name__ == "__main__":
    main()
