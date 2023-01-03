"""
Compute the entropy in bits of a list of probabilities.
"""

import numpy as np


def entropy(ps):
    """
    Compute the entropy in bits of a list of probabilities.

    The input list of probabilities must sum to one and no
    element should be larger than 1 or less than 0.

    :param list ps: list of probabilities
    :type ps: list
    """
    if any([(p < 0.0) or (p > 1.0) for p in ps]):
        raise ValueError("At least one input is out of range [0...1]")
    else:
        pass
    if not np.isclose(1, np.sum(ps), atol=1e-08):
        raise ValueError("The list of input probabilities does not sum to 1")
    else:
        pass
    items = ps * np.log2(ps)
    new_items = []
    for item in items:
        if np.isnan(item):
            new_items.append(0)
        else:
            new_items.append(item)
    return np.abs(-np.sum(new_items))
