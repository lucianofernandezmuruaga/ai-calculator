from src.calculator import add_numbers

def test_add_positive_numbers():
    assert add_numbers(10, 5) == 15

def test_add_negative_numbers():
    assert add_numbers(-1, -1) == -2