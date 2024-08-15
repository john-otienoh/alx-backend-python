#!/usr/bin/env python3
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    '''
    type-annotated function to_kv
    that takes a string k and an int OR float v as arguments
    returns a tuple.
    '''
    return k, v ** 2
