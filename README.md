# CCRP-Lite Dataset (v0.1)
Small, educational dataset + script to illustrate the CCRP loop: **Collapse → Paradox Processing → Rebuild**.

## Files
- `ccrp_lite_dataset_v0_1.json` — 7 labeled scenarios with `entropy_score` and `fidelity_gain`.
- `analyze_ccrp_lite.py` — prints per-item summary, aggregates, and correlation.

## Purpose
- Demo for governance researchers and engineers.
- Seed for future fine-tuning datasets (turn scenarios into supervised Q&A or policy-choice tasks).
- Public-safe: no personal logs; high-level abstractions only.

## Run
```bash
python analyze_ccrp_lite.py

License

MIT (educational/research use). Please cite if you fork/extend.
