"""Quick Sort Algorithm

Divide and Conquer Paradigm
- Select a "pivot" element from array and partition other elements into 2 sub-arrays according to whether tey are less than or greater than the pivot
- Sub-arrays are recursively sorted

1. Select a pivot element from the array (common choices are 1st, last or middle element)
2. Rearrange array elements so that elements less than pivot are on the left, and elements greater than pivot are on the right. (Pivot is not in its final sorted position)
3. Recursively apply QuickSort to the sub-arrays on the left and right of the pivot
4. Base Case for recursion: sub-array has <= 1 elements, so it is sorted

Time Complexity: O(n log n)
- Actually could be O(n^2) worst case but on average, is O(n log n)

Space Complexity: O(log n)
- Recursively adding calls to the call stack
"""


def bubble_sort(lst: list[int]) -> list[int]:
    """Sorts list of integers

    :param lst: an unsorted list of integers
    :return: sorted list of integers
    """
    raise NotImplementedError("Implement logic for quick sort algorithm")
