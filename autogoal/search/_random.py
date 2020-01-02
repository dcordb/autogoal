# coding: utf8

import random

from ._base import SearchAlgorithm
from autogoal.grammar import Sampler


class RandomSearch(SearchAlgorithm):
    def __init__(self, grammar, fitness_fn, *, random_state: int = None):
        super(RandomSearch, self).__init__(grammar, fitness_fn)
        self._sampler = Sampler(random_state)

    def _run_one_generation(self, max_evaluations):
        yield self._grammar.sample(sampler=self._sampler)
