# Reproducibility Matrix

This release keeps algorithms source-grounded in the current research checkout. Raw third-party datasets and large
intermediate matrices are not committed.

| Paper component | Release status | Entry point | Source provenance |
| --- | --- | --- | --- |
| Main synthetic simulation | Included for DRO, CORD, and k-means methods available in this checkout | `scripts/run_synthetic_experiments.py --scenario main` | `code/subspace_clustering/simulation.py`, `code/subspace_clustering/subspace_clustering.py`, `code/portfolio-backtesting/portfolio_backtesting/stock_selection/cord.py` |
| Common-factor sweep | Included for source-grounded methods | `scripts/run_synthetic_experiments.py --scenario common-factor` | Same synthetic generator and method calls as above |
| Noise sweep and no-global-factor simulation | Included for source-grounded methods | `scripts/run_synthetic_experiments.py --scenario noise` and `--scenario additional` | Same synthetic generator and method calls as above |
| Ablation studies | Included | `scripts/run_ablation_studies.py --ablation all` | `code/ablation_studies.py` and core DRO routines |
| Extended Yale B face clustering | Included for DRO and the current CORD implementation; raw images are not redistributed | `scripts/run_face_experiments.py --data-dir data/external/CroppedYalePNG` | `code/image_dataset/image_experiments.ipynb` preprocessing, split generation, and method dispatch |
| Financial portfolio backtest | Documented, not repackaged as a standalone script in this cleanup pass | `docs/portfolio_experiment.md` | `code/subspace_clustering/portfolio.py`, `portfolio_analysis.ipynb`, and the nested `portfolio-backtesting` package |

Several comparison baselines in the manuscript relied on external packages or an older installed `portfolio_backtesting`
API that is referenced by notebooks but is not present as source in the current checkout. Those baselines are documented
rather than reimplemented, to avoid introducing unverified substitute algorithms.
