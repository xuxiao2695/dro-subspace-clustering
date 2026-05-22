"""
FILE: __init__.py
INPUT: Public imports from the dro_subspace package.
OUTPUT: Stable package-level API for release scripts.
POS: Package API boundary.
NOTE: Update this header and the folder's _MANIFEST.md explicitly if logic changes.
"""

from dro_subspace.dro import compute_dro_coefficients, dro_sqrt_delta, spectral_regression_admm
from dro_subspace.metrics import ClusteringScore, clustering_score, spectral_clustering
from dro_subspace.synthetic import make_cluster_labels, normalize_design, sample_cluster_sizes, sample_random_subspace

__all__ = [
    "ClusteringScore",
    "clustering_score",
    "compute_dro_coefficients",
    "dro_sqrt_delta",
    "make_cluster_labels",
    "normalize_design",
    "sample_cluster_sizes",
    "sample_random_subspace",
    "spectral_clustering",
    "spectral_regression_admm",
]
