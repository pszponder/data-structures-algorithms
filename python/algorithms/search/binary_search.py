"""Binary Search Algorithm

CAUTION: Binary search requires the input list to be sorted (or needs to sort the list first before proceeding with the search)

Repeatedly divide search domain in half, and keep searching for the value in the middle of each search domain until a value is found.

1. Define 2 pointers to point to bounds of search domain (left ptr points to start of list, right ptr points to end)
2. Calculate middle element of current search domain based on pointers (can compute a mid pointer)
3. Compare middle element w/ target element
    a. If middle element is equal to target, search is successful
    b. If middle element less than target, update left pointer to middle + 1 and search right half of current search domain
    c. If middle element greater than target, update right pointer to middle - 1 and search left half of current search domain
4. Repeat steps 2 - 3 until target is found or search interval becomes empty (left pointer > right pointer)


Time Complexity: O(log n)
- ASSUMPTION: Ignore case where we would first need to sort binary search, since that could cause time complexity to worsen depending on sorting algorithm used.
- With each comparison, search space is halved
- In each step, algorithm either finds the target element or eliminates half of the remaining elements from consideration

Space Complexity: O(1)
- Don't create any data structures in the algorithm
"""


def binary_search(lst: list[int], target: int) -> int:
    """Searches input list for target integer

    :param lst: a list of integers
    :param target: target integer to find in the list (lst)
    :return: index of target in lst if found, -1 otherwise
    """
    raise NotImplementedError("Implement logic for binary search algorithm")
