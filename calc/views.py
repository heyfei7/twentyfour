# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from calc.models.game import TwentyFour


def index(request):
    game = TwentyFour(4)
    context = {"numbers": game.numbers,
               "solution": game.solution,
               "target": game.TARGET}
    return render(request, "index.html", context)