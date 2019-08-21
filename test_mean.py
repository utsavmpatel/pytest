from mean import *

def test_ints():
    num_list = [2,3,4]
    obs = 3
    exp = mean(num_list)
    assert obs == exp

def test_zero():
    num_list = [3,0,5,4]
    obs = 3
    exp = mean(num_list)
    assert obs == exp

def test_neg():
    num_list = [3,4,8,-3]
    obs = 3
    exp = mean(num_list)
    assert obs == exp



