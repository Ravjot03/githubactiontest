from src.math_operations import add, sub

def test_add():
    assert add(2,3)==5
    assert add(5,4)==9

def test_sub():
    assert sub(5,1)==4
    assert sub(1,3)==-2