import pytest


def my_func_test():
    return "Pass the test."


def test_test():
    assert my_func_test() == "Pass the test."
