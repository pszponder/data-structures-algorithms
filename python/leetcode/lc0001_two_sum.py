"""
1. Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

===========
APPROACHES:
===========

-----------------------
Approach 1: Brute Force
-----------------------
Nested loop to loop through all combinations of sums.
Return the indices of the values whose sum equals the target.

Time Complexity: O(n^2)
- Nested loop is O(n^2)

Space Complexity: O(1)
- We aren't storing any data structures to keep track of the sum

----------------------
Approach 2: 2-Pointers
----------------------
1. Sort the array
2. Position a pointer at each end of the array
3. Sum the values which the pointers are referencing
4. If the sum is smaller than the target, move the left pointer to the right (to a larger number)
5. If the sum is greater than the target, move the right pointer to the left (to a smaller number)
6. Repeat moving the pointers towards each other until the sum is found
7. Once the sums are found, go back and find the indices of the two values

Time Complexity: O(n log n)
- Sorting is O(n log n)
- Moving pointers towards each other is O(n)
- Finding index of each value is O(n)
- O(n log n) worse than O(n)

Space Complexity: O(1)
- O(1) since not creating any data structures

--------------------
APPROACH 3: Hash Map
--------------------
NOTE: Solution from https://www.youtube.com/watch?v=KLlXCFG5TnA&t=1s
1. Initialize an empty map. This map will contain each list value and the index of the value
2. Iterate over the elements in the list
3. For each element, compute difference between target and current value
4. If the difference is in the hash map, return the index of the current value and the index of the number needed for the difference
5. Otherwise, add the current number & index to the map

Time Complexity: O(n)
- Iterate through the list once

Space Complexity: O(n)
- Building a map of size n
"""


def two_sum1(nums: list[int], target: int) -> list[int]:
    """Approach 1: Brute Force"""
    for i, num_x in enumerate(nums):
        for j, num_y in enumerate(nums):
            if i != j and num_x + num_y == target:
                return [i, j]
    return []


def two_sum2(nums: list[int], target: int) -> list[int]:
    """Approach 2: 2-Pointers"""

    # Setup index position of pointers
    lptr = 0  # Left Pointer
    rptr = len(nums) - 1  # Right Pointer

    # Sort the list
    sorted_nums = sorted(nums)

    # Keep iterating until the pointers cross each other
    while lptr < rptr:
        num_sum = sorted_nums[lptr] + sorted_nums[rptr]

        if num_sum == target:
            # If sum at pointers matches target, find the original index of the pointers
            idx1 = nums.index(sorted_nums[lptr])
            idx2 = nums.index(sorted_nums[rptr])

            # idx1 can't equal idx2
            if idx1 == idx2:
                idx2 = nums.index(sorted_nums[rptr], idx1 + 1)

            # in case we have negative numbers in array, flip positions of idx1 and idx2
            if idx1 > idx2:
                idx1, idx2 = idx2, idx1

            return [idx1, idx2]
        elif num_sum < target:
            # If sum less than target, need larger sum, move lptr right
            lptr += 1
        else:
            # If sum greater than target, need smaller sum, move rptr to left
            rptr -= 1

    return []


def two_sum3(nums: list[int], target: int) -> list[int]:
    """Approach 3: Hash map"""
    seen = {}  # value : index

    for i, n in enumerate(nums):
        # Compute the difference needed to complete target sum w/ current number
        diff = target - n

        if diff in seen:
            # If the diff is found, return the indices
            return [seen[diff], i]
        # Otherwise, keep going and add the current value & index to the hash map
        seen[n] = i
    return []
