from src.math_op import add,sub
def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    assert add(5,3)==8

def test_sub():
    assert sub(5,3)==2
    assert sub(4,4)==0