from api.common.util import calculator


def test_calculator():
    res = calculator(2, 4)
    assert res == 6
