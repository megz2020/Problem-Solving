#test cases for is_valid_subsequence.py
from solution1 import is_valid_subsequence as is_valid_subsequence1
from solution2 import is_valid_subsequence as is_valid_subsequence2

def test_is_valid_subsequence():
    array = [5,1,22,25,6,-1,8,10]
    sequence = [1,6,-1,10]
    assert is_valid_subsequence1(array, sequence) == True
    assert is_valid_subsequence2(array, sequence) == True

    array = [5,1,22,25,6,-1,8,10]
    sequence = [5,1,22,25,6,-1,8,10]
    assert is_valid_subsequence1(array, sequence) == True
    assert is_valid_subsequence2(array, sequence) == True

    array = [5,1,22,25,6,-1,8,10]
    sequence = [5,1,22,6,-1,8,10]
    assert is_valid_subsequence1(array, sequence) == True
    assert is_valid_subsequence2(array, sequence) == True

    array = [5,1,22,25,6,-1,8,10]
    sequence = [22,25,6]
    assert is_valid_subsequence1(array, sequence) == True
    assert is_valid_subsequence2(array, sequence) == True

    array = [5,1,22,25,6,-1,8,10]
    sequence = [1,6,10]
    assert is_valid_subsequence1(array, sequence) == True
    assert is_valid_subsequence2(array, sequence) == True

    array = [5,1,22,25,6,-1,8,10]
    sequence = [5,1,22,10]
    assert is_valid_subsequence1(array, sequence) == True
    assert is_valid_subsequence2(array, sequence) == True

    array = [5,1,22,25,6,-1,8,10]
    sequence = [5,1,25,22,6,-1,8,10]
    assert is_valid_subsequence1(array, sequence) == False
    assert is_valid_subsequence2(array, sequence) == False

    array = [5,1,22,25,6,-1,8,10]
    sequence = [5,1,22,6,-1,8,10,12]
    assert is_valid_subsequence1(array, sequence) == False
    assert is_valid_subsequence2(array, sequence) == False

