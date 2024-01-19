"""Merge Sort Algorithm

Divide and Conquer Sorting

1. DIVIDE: Recursively divide the input array into 2 halves until each sub-array contains at most one element
2. CONQUER: Sort the individual elements (or sub-arrays) by comparing and merging them in a way that builds a sorted sequence
3. COMBINE: Merge the sorted sub-arrays back together to form a single sorted array

Time Complexity: O(n log n)
- Dividing array into smaller sub-arrays is O(log n)
- Merging sub-arrays back together is O(n)

Space Complexity: O(n)
- Create 2 additional arrays to store left and right halves of input during each recursive call
- Memory required to store arrays increases linearly w/ the size of the input
"""


def merge_sort(lst: list[int]) -> list[int]:
    """Sorts list of integers

    :param lst: an unsorted list of integers
    :return: sorted list of integers
    """
    raise NotImplementedError("Implement logic for merge sort algorithm")
