"""
FILE: test_core.py
INPUT: Small deterministic synthetic examples.
OUTPUT: Release smoke tests for generation and clustering metrics.
POS: Test coverage for public helper APIs.
NOTE: Update this header and the folder's _MANIFEST.md explicitly if logic changes.
"""

from __future__ import annotations

import numpy as np

from dro_subspace.metrics import clustering_score
from dro_subspace.synthetic import make_cluster_labels, normalize_design, sample_random_subspace


def test_sample_random_subspace_is_deterministic() -> None:
    first, *_ = sample_random_subspace(
        n_samples=12,
        n_variables=8,
        cluster_sizes=[4, 4],
        n_group_factors=1,
        rho_range=(0.0, 0.1),
        noise_range=(0.1, 0.2),
        seed=7,
    )
    second, *_ = sample_random_subspace(
        n_samples=12,
        n_variables=8,
        cluster_sizes=[4, 4],
        n_group_factors=1,
        rho_range=(0.0, 0.1),
        noise_range=(0.1, 0.2),
        seed=7,
    )
    assert np.allclose(first, second)
    assert normalize_design(first).shape == (12, 8)


def test_clustering_score_is_permutation_invariant() -> None:
    true_labels = make_cluster_labels([2, 3, 1])
    predicted_labels = np.array([2, 2, 0, 0, 0, 1])
    score = clustering_score(true_labels, predicted_labels)
    assert score.error_rate == 0.0
    assert score.accuracy == 1.0
    assert score.adjusted_mutual_information == 1.0
