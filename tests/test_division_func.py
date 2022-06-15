#!/usr/bin/env python3
import sys
sys.path.append('D:\\coding\\pytest\\funcs')
import division_func
import pytest


@pytest.mark.parametrize('dividend, divisor, expected_result', [
    (10, 2, 5),
    (20, 10, 2),
    (30, -3, -10),
    (5, 2, 2.5)
    ])
def test_division_func_good(dividend, divisor, expected_result):
    print(division_func.division_func(dividend, divisor))
    assert division_func.division_func(dividend, divisor) == expected_result


@pytest.mark.parametrize('expected_exception, dividend, divisor', [
    (ZeroDivisionError, 10, 0),
    (TypeError, 10, '2'),
    ])
def test_division_func_with_error(expected_exception, dividend, divisor):
    with pytest.raises(expected_exception):
        division_func.division_func(dividend, divisor)
