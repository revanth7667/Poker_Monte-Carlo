""" To Test the main codes"""

from example import custom_add

def test_example():
    """test cases"""
    assert custom_add(2,3) == 5
    assert custom_add(4,5) == 9
    assert custom_add(-1,1) == 0
    assert custom_add(-1,-3) == -4
    assert custom_add(0,0) == 0

test_example()
