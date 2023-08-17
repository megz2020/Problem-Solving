#This inspird by ALgoexpert
# The complexity of this solution is O(n^2) time | O(1) space
#explaination time complexity and space complexity
# time complexity is O(n^2) because we are iterating through the array which is O(n) and 
#then we are iterating through the array again which is O(n) so total = O(n) * O(n) = O(n^2)
# space complexity is O(1) because we are not using any extra space

from typing import List


def two_sum(array: List[int], target: int) -> List[int]:
    """
    Get a pair of numbers from the given list that sum up to the target.

    Args:
        array (List[int]): The list of integer values.
        target (int): The target sum of two numbers.

    Returns:
        List[int]: A list containing two numbers from the array that add up to the target.
                   If no such pair exists, an empty list is returned.
    Raises:
        Exception: If the input array is not of type list or if the target is not of type int.
    """
    if not isinstance(array, list):
        raise Exception("Input array must be of type list.")
    if not isinstance(target, int):
        raise Exception("Target must be of type int.")

    res = []
    len_array = len(array)
    for i in range(len_array -1):
        for j in range(i+1, len_array):
            potintial_sum = array[i] +array[j]
            if potintial_sum == target:
                res = [array[i], array[j]]
                return res
    return res



if __name__ == "__main__":
    array = [3,5,-4,8,11,1,-1,6]
    target = 10
    print(two_sum(array, target))
