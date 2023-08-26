Two-pointer technique

This pattern is widely applicable to various algorithmic problems that involve finding pairs of elements, subsets, or values that satisfy certain conditions.

## classic problems

* Two Sum
* Trapping Rain Water
* Remove Duplicates from Sorted Array
* Product of Array Except Self
* valid palindrome
* Reverse Words in a String

## soulution
 To implement soulution(This genaric but not applicable to all problems) we need to follow the following steps:
 - we can use two pointers to scan the array from both left and right ends. In this case the complexity would be O(NlogN) due to sorting and the space complexity would be O(1) because we don’t need any extra space.
 - we can use hash map to store the value and index of the array elements. In this case the complexity would be O(N) and the space complexity will also be O(N) because we need to store N elements in the hash map.