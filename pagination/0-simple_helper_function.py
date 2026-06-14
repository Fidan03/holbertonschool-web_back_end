#!/usr/bin/env python3
"""Simple helper function for pagination index range."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of (start_index, end_index) for the given page."""
    start = (page - 1) * page_size
    return (start, start + page_size)
