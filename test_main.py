import pytest


def a_method():
    raise Exception()


def test_sample_method():
    with pytest.raises(Exception):
        a_method()
