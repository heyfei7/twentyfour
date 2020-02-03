# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import operator


class Equation:
    OPERATIONS = {"+": operator.add,
                  "-": operator.sub,
                  "*": operator.mul,
                  "/": operator.truediv}

    def __init__(self, o, l, r):
        self.operator = o   # str, represents an operator
        self.left = l       # int or Equation
        self.right = r      # int or Equation

    def __str__(self):
        return "(" + " ".join([str(self.left),self.operator, str(self.right)]) + ")"

    def eval(self):
        left = self.left if isinstance(self.left, int) else self.left.eval()
        right = self.right if isinstance(self.right, int) else self.right.eval()
        if self.operator == "/" and right == 0:
            return False
        return Equation.OPERATIONS[self.operator](left, right)