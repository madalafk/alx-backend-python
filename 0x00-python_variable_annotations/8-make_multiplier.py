#!/usr/bin/nv python3
'''
type-annotated function make_multiplier
'''
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    takes a float multiplier as argument and returns a function
    that multiplies a float by multiplier.
    '''
    def f(n: float) -> float:
        """ multiplies a float by multiplier """
        return float(n * multiplier)

    return f
