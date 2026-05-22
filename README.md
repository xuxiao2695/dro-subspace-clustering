# DRO Subspace Clustering

Reference code for the ICML submission on distributionally robust subspace clustering. The repository contains the synthetic-data generator, DRO spectral self-regression solver, clustering metrics, and ablation scripts used for the paper.

## Setup

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e .
```

## Reproduce

```bash
python scripts/run_ablation_studies.py --ablation all --n-experiments 10
```

Results are written to `results/ablation_results/`. The checked-in CSV files are small summary outputs; large intermediate matrices and raw datasets are intentionally excluded.
Use `--max-outer-iterations` to raise or lower the bounded ADMM convergence budget.

## Data

Synthetic experiments generate their own data. External datasets used in exploratory notebooks are not redistributed here for copyright reasons. See `data/README.md` for links and expected local placement.
