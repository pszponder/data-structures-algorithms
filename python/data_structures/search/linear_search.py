"""
Linear Search Algorithm

Time Complexity: O(n)
- If input array is n long, then we potentially need to traverse the whole array before finding the target

Space Complexity: O(1)
- Don't create any data structures in the algorithm
"""


def linear_search(lst: list[int], target: int):
    """Searches input list for target integer

    :param lst: a list of integers
    :param target: target integer to find in the list (lst)
    :return: index of target in lst if found, -1 otherwise
    """
    for idx, value in enumerate(lst):
        if value == target:
            return idx
    return -1
