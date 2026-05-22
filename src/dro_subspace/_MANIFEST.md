Update me whenever files in this folder change.
Core package split by data generation, clustering metrics, DRO optimization, and experiment orchestration.
- `__init__.py`: public package exports.
- `dro.py`: DRO delta calibration and bounded spectral ADMM solver.
- `experiments.py`: reproducible ablation experiment runners with solver-budget configuration.
- `metrics.py`: spectral clustering and clustering-score utilities.
- `synthetic.py`: synthetic random-subspace data generation and preprocessing.
