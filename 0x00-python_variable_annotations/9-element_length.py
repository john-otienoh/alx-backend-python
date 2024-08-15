#!/usr/bin/env python3
from typing import Tuple, Iterable


def element_length(lst: Iterable[str]) -> list[Tuple[int, int]]:
    return [(i, len(i)) for i in lst]
