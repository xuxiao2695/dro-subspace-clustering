# DRO Subspace Clustering

Reference code for the ICML submission on distributionally robust subspace clustering. The repository contains the synthetic-data generator, DRO spectral self-regression solver, source-grounded CORD helper, clustering metrics, and reproduction scripts for the compact release.

## Setup

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e .
```

## Reproduce

```bash
python scripts/run_ablation_studies.py --ablation all --n-experiments 10
python scripts/run_synthetic_experiments.py --scenario main --n-experiments 10
python scripts/run_face_experiments.py --data-dir data/external/CroppedYalePNG
```

Results are written to `results/`. The checked-in CSV files are small summary outputs; large intermediate matrices and raw datasets are intentionally excluded.
Use `--max-outer-iterations` to raise or lower the bounded ADMM convergence budget.
See `docs/reproducibility_matrix.md` for the mapping from paper experiments to release commands and known source gaps.
The financial backtest is documented in `docs/portfolio_experiment.md` because the raw WRDS-derived data and older local
backtesting API are not safely redistributable from this checkout.

## Data

Synthetic experiments generate their own data. External datasets used in exploratory notebooks are not redistributed here for copyright reasons. See `data/README.md` for links and expected local placement.
