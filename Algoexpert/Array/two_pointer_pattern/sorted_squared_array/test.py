# test cases for sorted_squared_array.py
from solution1 import sortedSquaredArray as sortedSquaredArray1
from solution2 import sortedSquaredArray as sortedSquaredArray2

def test_sorted_squared_array():

    array = [1,2,3,5,6,8,9]
    assert sortedSquaredArray1(array) == [1,4,9,25,36,64,81]
    assert sortedSquaredArray2(array) == [1,4,9,25,36,64,81]

    array = [-10,-5,0,5,10]
    assert sortedSquaredArray1(array) == [0,25,25,100,100]
    assert sortedSquaredArray2(array) == [0,25,25,100,100]

    #test case for empty array
    array = []
    assert sortedSquaredArray1(array) == []
    assert sortedSquaredArray2(array) == []


    #test case for non array input raises exception
    array = 1
    try:
        sortedSquaredArray1(array)
    except Exception as e:
        assert str(e) == "Input array must be of type list."

    try:
        sortedSquaredArray2(array)
    except Exception as e:
        assert str(e) == "Input array must be of type list."


if __name__ == "__main__":
    test_sorted_squared_array()