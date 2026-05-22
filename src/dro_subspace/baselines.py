"""
FILE: baselines.py
INPUT: Normalized sample matrices and baseline method settings.
OUTPUT: Source-grounded non-DRO baseline cluster labels.
POS: Optional baseline wrappers for ICML experiment reproduction scripts.
NOTE: Update this header and the folder's _MANIFEST.md explicitly if logic changes.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

IntArray = NDArray[np.int_]
FloatArray = NDArray[np.float64]


def kmedoids_clustering(samples: FloatArray, n_clusters: int) -> IntArray:
    """Run the pyclustering k-medoids baseline from the old simulation scripts."""
    try:
        from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
        from pyclustering.cluster.kmedoids import kmedoids
    except ModuleNotFoundError as exc:
        message = "Install optional baseline dependencies with `pip install -e '.[baselines]'`."
        raise ModuleNotFoundError(message) from exc

    corr = np.corrcoef(samples.T)
    distance = 1.0 - corr**2
    initial_medoids = kmeans_plusplus_initializer(
        samples.T,
        n_clusters,
        kmeans_plusplus_initializer.FARTHEST_CENTER_CANDIDATE,
    ).initialize(return_index=True)
    instance = kmedoids(distance, initial_medoids, data_type="distance_matrix")
    instance.process()
    clusters = instance.get_clusters()
    membership = np.full(samples.shape[1], -1, dtype=int)
    for cluster_idx, cluster in enumerate(clusters):
        for variable_idx in cluster:
            membership[variable_idx] = cluster_idx
    if np.any(membership < 0):
        raise RuntimeError("k-medoids did not assign every variable to a cluster.")
    return membership
