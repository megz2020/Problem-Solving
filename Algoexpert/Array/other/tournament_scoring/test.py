## Test cases for tournament_scoring.py

from solution1 import tournment_winner as tournment_winner1
from solution2 import tournment_winner as tournment_winner2

def test_tournment_winner():
    compition = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
    results = [0, 0, 1]
    assert tournment_winner1(compition, results) == "Python"
    assert tournment_winner2(compition, results) == "Python"

    compition = [["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"]]
    results = [0, 1, 1]
    assert tournment_winner1(compition, results) == "Java"
    assert tournment_winner2(compition, results) == "Java"

    compition = [["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"]]
    results = [0, 0, 0]
    assert tournment_winner1(compition, results) == "Java"
    assert tournment_winner2(compition, results) == "Java"


    # raise exception if the number of competitions is not equal to the number of results
    compition = [["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"]]
    results = [1, 1]
    try:
        tournment_winner1(compition, results)
    except Exception as e:
        assert str(e) == "The number of competitions is not equal to the number of results"
    
    try:
        tournment_winner2(compition, results)
    except Exception as e:
        assert str(e) == "The number of competitions is not equal to the number of results"

    # raise exception if the type of the input is not correct
    compition = [["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"]]
    results = "1, 1, 1"
    try:
        tournment_winner1(compition, results)
    except Exception as e:
        assert str(e) == "The type of the input is not correct"

    try:
        tournment_winner2(compition, results)
    except Exception as e:
        assert str(e) == "The type of the input is not correct"


if __name__ == '__main__':
    test_tournment_winner()
    print("All tests passed")

