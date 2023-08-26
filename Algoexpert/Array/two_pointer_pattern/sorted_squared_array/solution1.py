#This inspird by ALgoexpert
# The complexity of this solution is O(nlog(n)) time | O(n) space
#explaination time complexity and space complexity
# time complexity is O(nlog(n)) because we are iterating through the array which is O(n) and
#then we sorting the array which is O(nlog(n)) so total = O(n) + O(nlog(n)) = O(nlog(n))
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
	
    squared_array = [0 for _ in array]
    for index in range(len(array)):
        squared_value = array[index] * array[index]
        squared_array[index] = squared_value


    squared_array.sort() 
    return squared_array





if __name__ == "__main__":
    array = [1,2,3,5,6,8,9]
    print(sortedSquaredArray(array))