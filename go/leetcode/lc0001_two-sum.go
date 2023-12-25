/*
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
*/

package leetcode

import "sort"

// Solution 1: Brute Force
func twoSum1(nums []int, target int) []int {
	for i := 0; i < len(nums)-1; i++ {
		for j := 1; j < len(nums); j++ {
			sNum := nums[i] + nums[j]
			if sNum == target {
				return []int{i, j}
			}
		}
	}
	return []int{}
}

// Solution 2: 2-Pointer
func twoSum2(nums []int, target int) []int {
	// Create a deep copy of original slice & copy elements from original slice into new slice
	sorted := make([]int, len(nums))
	copy(sorted, nums)

	// Sort the copy
	sort.Ints(sorted)

	lPtr := 0
	rPtr := len(nums) - 1

	// Keep iterating until pointers cross
	for lPtr < rPtr {
		sum := sorted[lPtr] + sorted[rPtr]
		if sum == target {
			// target sum has been found, find and return the indices
			idx1 := findIdx(nums, sorted[lPtr])
			idx2 := findIdx(nums, sorted[rPtr])

			// If values at idx1 & idx2 are the same, then find the next index for idx2
			if nums[idx1] == nums[idx2] {
				idx2 = findIdx(nums, sorted[rPtr], idx1+1)
			}

			// If sorted arrays has negative numbers, swap idx1 & idx2
			if idx1 > idx2 {
				idx1, idx2 = idx2, idx1
			}

			return []int{idx1, idx2}
		} else if sum < target {
			// Move left pointer up
			lPtr++
		} else {
			// (sum > target) Move right pointer down
			rPtr--
		}
	}

	return []int{}
}

// findIdx returns the index given an int slice and a target value
// Pass in an optional start index
// This is a helper function used by twoSum2
func findIdx(nums []int, target int, startIndices ...int) int {
	startIdx := 0
	if len(startIndices) > 0 {
		startIdx = startIndices[0]
	}

	for idx := startIdx; idx < len(nums); idx++ {
		if nums[idx] == target {
			return idx
		}
	}

	return -1 // Return -1 if target not found
}

// Solution 3: Hash Map
func twoSum3(nums []int, target int) []int {
	// Store each num & its index in the map
	hashMap := make(map[int]int) // num : idx

	// Iterate through nums
	for idx, num := range nums {
		// Compute the diff needed to complete target sum w/ current number
		diff := target - num

		// Check if the diff is in the map
		// Recall the hashmap keys are the numbers & the hashmap values are the indices of the numbers
		diffIdx, ok := hashMap[diff]
		if ok {
			// diff is found, return indices
			return []int{diffIdx, idx}
		}

		// If the diffIdx was not found,
		// add the current number & its index to the hashmap
		hashMap[num] = idx
	}

	return []int{}
}
