# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import random
import itertools
from .equation import Equation

class TwentyFour:
    MAX_NUM = 10
    TARGET = 24

    @staticmethod
    def solution(ordered_numbers, ordered_operations):
        for numbers in ordered_numbers:
            for ops in ordered_operations:
                eq = Equation(ops[0], numbers[0], numbers[1])
                for i in range(1, len(ops)):
                    eq = Equation(ops[i], eq, numbers[i + 1])
                if eq.eval() == 24:
                    return str(eq)
        return False

    def __init__(self, size):
        self.solution = False

        while not self.solution:
            self.numbers = [random.randint(0, TwentyFour.MAX_NUM) for i in range (0,size)]
            self.solution = TwentyFour.solution(list(itertools.permutations(self.numbers)),
                                                list(itertools.permutations(Equation.OPERATIONS.keys(), size-1)))