#!/usr/bin/env python3
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    type-annotated function make_multiplier
    takes a float multiplier as argument
    returns a function that multiplies a float by multiplier.
    '''
    def multiply(x: float) -> float:
        '''
        function that multiplies a float by multiplier.
        '''
        return x * multiplier
    return multiply
