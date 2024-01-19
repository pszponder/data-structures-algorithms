"""Bubble Sort Algorithm

Compare adjacent elements and swap them if they are in the wrong order

1. Start at the beginning of the list
2. Compare 2 elements
3. If the 1st element is greater than the 2nd, swap the position of the elements
4. Keep comparing pairs of elements until you get to the end of the list
5. Go back to the start of the list and keep comparing & swapping but don't sort last sorted element
6. Each iteration through the list is smaller by 1. Each iteration ends up sorting the hightest unsorted value

Time Complexity: O(n^2)
- Worst case is when list is sorted in reverse order
- Sort needs to make n - 1 passes through the entire list to move largest element to its correct position
- In 2nd pass, 2nd largest element is moved to its correct position
- Process repeats for all other values

Space Complexity: O(1)
- Only requires a constant amount of additional memory space for temp variables and swaps
"""


def bubble_sort(lst: list[int]) -> list[int]:
    """Sorts list of integers

    :param lst: an unsorted list of integers
    :return: sorted list of integers
    """
    raise NotImplementedError("Implement logic for bubble sort algorithm")
