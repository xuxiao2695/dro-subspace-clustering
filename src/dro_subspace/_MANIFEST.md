Update me whenever files in this folder change.
Core package split by data generation, source-grounded baselines, clustering metrics, DRO optimization, and experiment orchestration.
- `__init__.py`: public package exports.
- `cord.py`: CORD/ACC distance, greedy clustering, and membership helpers ported from the current source tree.
- `dro.py`: DRO delta calibration and bounded spectral ADMM solver.
- `experiments.py`: reproducible ablation experiment runners with solver-budget configuration.
- `images.py`: Extended Yale B preprocessing and split helpers ported from the face notebook.
- `metrics.py`: spectral clustering and clustering-score utilities.
- `synthetic.py`: synthetic random-subspace data generation and preprocessing.
