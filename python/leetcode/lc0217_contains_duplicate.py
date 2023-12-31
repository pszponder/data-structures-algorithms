"""
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/
https://leetcode.com/problems/contains-duplicate/solutions/3672475/4-method-s-c-java-python-beginner-friendly/

Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

===========
APPROACHES:
===========

-----------------------
Approach 0: Brute Force
-----------------------
Using a nested loop, compare each element to every other element in the array.

Time Complexity: O(n^2)
- The outer loop iterates through the array once
- The inner loop iterates through the array once for each element in the outer loop
- O(n) * O(n) = O(n^2)

Space Complexity: O(1)
- Don't create any new data structures

-----------------------
Approach 1: Using a Map
-----------------------
Approach 1: Using a Map
Build up a map of the numbers and their counts. If any count is greater than 1, return true.

Time Complexity: O(n)
- Iterate through the string once to build the map
- Iterate through the string again to compare the map values
- O(n) + O(n) = O(2n) = O(n)

Space Complexity: O(n)
- Create a map to store the characters and their counts
- The map will be the same size as the input string

-------------------
Approach 2: Sorting
-------------------
Sort the array and then iterate through it. If any two adjacent numbers are the same, return true.

Time Complexity: O(n log n)
- Sorting takes O(n log n) time
- Comparing the strings takes O(n) time
- O(n log n) + O(n) = O(n log n)

Space Complexity: O(n)
- Create a new array that is the same size as the input array
- O(n) + O(n) = O(2n) = O(n)

---------------------------
Approach 3: Using a Hashset
---------------------------
Keep track of whether or not a number has appeared more than once by putting the numbers in a set

Time Complexity: O(n)
- Iterate through the array once to add the numbers to the set
- Iterate through the array again to check if the numbers are in the set
- O(n) + O(n) = O(2n) = O(n)

Space Complexity: O(n)
- Create a set to store the numbers
- The set will be the same size as the input array
"""


def contains_duplicate0(nums: list[int]) -> bool:
    """
    Approach 0: Brute Force
    """
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False

    # LESS EFFICIENT THAN ABOVE
    # for idx1, num1 in enumerate(nums):
    #     for idx2, num2 in enumerate(nums):
    #         if idx1 != idx2 and num1 == num2:
    #             return True
    # return False


def contains_duplicate1(nums: list[int]) -> bool:
    """
    Approach 1: Using a Map
    """

    num_counts: dict[int, int] = {}
    for num in nums:
        if num in num_counts:
            return True
        else:
            num_counts[num] = 1
    return False


def contains_duplicate2(nums: list[int]) -> bool:
    """
    Approach 2: Sorting
    """

    sorted_list = sorted(nums)
    for idx in range(len(sorted_list) - 1):
        if sorted_list[idx] == sorted_list[idx + 1]:
            return True
    return False


def contains_duplicate3(nums: list[int]) -> bool:
    """
    Approach 3: Using a Set
    """

    hashset: set[int] = set()
    for num in nums:
        if num in hashset:
            return True
        else:
            hashset.add(num)
    return False
