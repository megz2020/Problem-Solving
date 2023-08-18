#This inspird by ALgoexpert
# The coplexity of this solution is O(n) time and O(1) space
#explanation of complexity:
# O(n) time because we are iterating through the array once
# O(1) space because we are not using any extra space, we are just using the input array and sequence

from typing import List

def is_valid_subsequence(array: List[int], sequence: List[int]) -> bool:
    """
    Checks if the given sequence is a valid subsequence of the array.

    Args:
        array (List[int]): The main array to check against.
        sequence (List[int]): The sequence to check for validity.

    Returns:
        bool: True if the sequence is a valid subsequence of the array, False otherwise.

    Raises:
        Exception: If the input array or sequence is not of type list or if the sequence is longer than the array.
    """
    if not isinstance(array, list):
        raise Exception("Input array must be of type list.")
    if not isinstance(sequence, list):
        raise Exception("Input sequence must be of type list.")
    if len(sequence) > len(array):
        return False
    
    array_index = 0
    sequence_index = 0
    array_length = len(array)
    sequence_length = len(sequence)

    while array_index < array_length and sequence_index < sequence_length:
        if sequence[sequence_index] == array[array_index]:
            sequence_index += 1

        array_index += 1

    return sequence_length == sequence_index



if __name__ == "__main__":
    array = [5,1,22,25,6,-1,8,10]
    sequence = [1,6,-1,10]
    print(is_valid_subsequence(array, sequence))