/*
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/
https://leetcode.com/problems/contains-duplicate/solutions/2552285/go-multiple-solutions-in-go-golang/

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


==========
APPROACHES
==========

-----------------------
APPROACH 0: Brute Force
-----------------------
Using a nested loop, compare each number to every other number in the array.

Time Complexity: O(n^2)
- Nested loop

Space Complexity: O(1)
- No extra space used

-----------------------
APPROACH 1: Using a map
-----------------------
Build up a map of the numbers and their counts. If any count is greater than 1, return true.

Time Complexity: O(n)
- Iterate through the array once (up to n)
- Map lookup is O(1)
- Map insertion is O(1)

Space Complexity: O(n)
- Map size is proportional to the number of elements in the array
- Worst case is all elements are unique, so map size is n

-------------------
APPROACH 2: Sorting
-------------------

Sort the array and then iterate through it. If any two adjacent numbers are the same, return true.

Time Complexity: O(n log n)
- Sorting is O(n log n)
- Iterating through the array is O(n)
- O(n log n) + O(n) = O(n log n)

Space Complexity: O(1)
- No extra space used
*/

package leetcode

import (
	"sort"
)

// Brute Force
func ContainsDuplicate0(nums []int) bool {
	// for i, num1 := range nums {
	// 	for j, num2 := range nums {
	// 		// Skip comparing the same element
	// 		if i != j && num1 == num2 {
	// 			return true
	// 		}
	// 	}
	// }
	// return false

	for i := 0; i < len(nums)-1; i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i] == nums[j] {
				return true
			}
		}
	}
	return false
}

// Using a map
func ContainsDuplicate1(nums []int) bool {
	// Define an empty map of ints to ints
	numCount := make(map[int]int)

	// Iterate through the nums array
	for _, num := range nums {
		// If the number is not in the map, add it with a count of 1
		if _, exists := numCount[num]; !exists {
			numCount[num] = 1
		} else {
			// If the number already exists in the map, then we have a duplicate and we are done
			return true
		}
	}

	return false
}

// Sorting
func ContainsDuplicate2(nums []int) bool {
	// Sort the array
	sort.Ints(nums)

	// Iterate through the array
	for i := 0; i < len(nums)-1; i++ {
		// If any two adjacent numbers are the same, return true
		if nums[i] == nums[i+1] {
			return true
		}
	}

	return false
}
