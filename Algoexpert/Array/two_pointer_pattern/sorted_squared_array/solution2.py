#This inspird by ALgoexpert
# The complexity of this solution is O(n) time | O(n) space
#explaination time complexity and space complexity
# time complexity is O(n) because we are iterating through the array which is O(n) and 
#reverse iterating through the array which is O(n) so total = O(n) + O(n) = O(n)
# space complexity is O(n) because we are using extra space to store the squared values of the array
from typing import List

def sortedSquaredArray(array: List[int]) -> List[int]:
    """Get a sorted array of squared values from the given array.

    Args:
        array : The list of integer values.
    Returns:
        List[int]: A list containing squared values of the input array.
    Raises:
        Exception: If the input array is not of type list.
    """

    if not isinstance(array, list):
        raise Exception("Input array must be of type list.")
    
    if len(array) == 0:
        return array

    sorted_squared_array = [0 for _ in array]
    left_index = 0
    right_index = len(array) - 1

    for index in reversed(range(len(array))):
        if abs(array[left_index]) > abs(array[right_index]):
            sorted_squared_array[index] = array[left_index] * array[left_index]
            left_index += 1
        else:
            sorted_squared_array[index] = array[right_index] * array[right_index]
            right_index -= 1

    return sorted_squared_array


if __name__ == "__main__":
    array = [1,2,3,5,6,8,9]
    print(sortedSquaredArray(array))