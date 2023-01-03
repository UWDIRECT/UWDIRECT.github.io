"""
Tests for the entropy function
"""

import numpy as np
import unittest

from entropy import entropy


class TestEntropy(unittest.TestCase):

    def test_smoke(self):
        """
        Simple smoke test to make sure function runs.
        """
        entropy([1])
        return

    def test_args_dont_sum_to_1(self):
        """
        Edge test to make sure the function throws a ValueError
        when the input probabilities do not sum to one.
        """
        with self.assertRaises(ValueError):
            entropy([.9, .9])
        return

    def test_args_out_of_range(self):
        """
        Edge tst to make sure the function throws a ValueError
        when the input probabilities are < 0 or > 1.
        """
        with self.assertRaises(ValueError):
            entropy([-1, 2])
        return

    def test_four_equal_likelihood_states(self):
        """
        One shot test using the known case of four states with
        equal likelihood of occurrence. Should return 2 bits.
        """
        assert np.isclose(entropy([0.25, 0.25, 0.25, 0.25]), 2.)
        return

    def test_equal_probability(self):
        """
        Pattern test using the known relationship of equal probabilities
        and predefined result.
        """
        def test(count):
            prob = 1.0/n
            ps = np.repeat(prob, n)
            assert np.isclose(entropy(ps), -np.log2(prob))
            return

        # run the test for a large number of iterations
        for n in range(10, 100000, 10000):
            test(n)
        return
