#This inspird by ALgoexpert
# The complexity of this solution is O(nlog(n)) time | O(1) space
#explaination time complexity and space complexity
# time complexity is O(nlog(n)) because we are sorting the array and then 
#we are iterating through the array which is O(n) and the sorting is O(nlog(n)) so total = O(nlog(n)) + O(n) = O(nlog(n))
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
    
    lef_arrow = 0
    right_arrow = len(array)-1
    array.sort()
    while lef_arrow < right_arrow:
        potintial_sum = array[lef_arrow] + array[right_arrow]
        
        if potintial_sum == target:
            return [array[lef_arrow] , array[right_arrow]]
        
        elif potintial_sum > target:
            right_arrow -= 1
        
        else:
            lef_arrow += 1

    return []


if __name__ == "__main__":
    array = [3,5,-4,8,11,1,-1,6]
    target = 10
    print(two_sum(array, target))