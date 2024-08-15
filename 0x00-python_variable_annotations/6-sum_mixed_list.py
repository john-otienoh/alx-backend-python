#!/usr/bin/env python3
from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    '''
    type-annotated function sum_mixed_list
    that takes a list mxd_lst of integers and floats
    returns their sum as a float.
    '''
    return float(sum(mxd_lst))
