#This inspird by ALgoexpert
# The complexity of this solution is O(n) time | O(n) space
#explaination time complexity and space complexity
# time complexity is O(n) because we are iterating through the array which is O(n)
# space complexity is O(n) because we are using a hash table to store the values


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
    nums = {}
    if not isinstance(array, list):
        raise Exception("Input array must be of type list.")
    if not isinstance(target, int):
        raise Exception("Target must be of type int.")

    for index, num in enumerate(array):
        potential_number = target - num
        if potential_number in nums:
            return [num, potential_number]

        else :
            nums[num] = index


    return []




if __name__ == "__main__":
    array = [3,5,-4,8,11,1,-1,6]
    target = 10
    print(two_sum(array, target))