/*
242. Valid Anagram

https://leetcode.com/problems/valid-anagram/description/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

===========
APPROACHES:
===========

-----------------------
Approach 1: Using a Map
-----------------------
Build up a map of the numbers and their counts. If any count is greater than 1, return true.

Time Complexity: O(n)
- Iterate over the string once to build the map
- Iterate over the string again to compare the values in the map
- O(n) + O(n) = O(2n) = O(n)

Space Complexity: O(n)
- The map will contain at most n entries

-------------------
Approach 2: Sorting
-------------------
Sort the strings and compare them. If they are the same, return true.

Time Complexity: O(n log n)
- Sorting the strings takes O(n log n) time
- Comparing the strings takes O(n) time
- O(n log n) + O(n) = O(n log n)

Space Complexity: O(n)
- The sorted strings will contain at most n characters
*/

package leetcode

import (
	"sort"
	"strings"
)

// Using a Map
func IsAnagram1(s, t string) bool {
	// Edge Case: Strings aren't same length
	if len(s) != len(t) {
		return false
	}

	// Create & Populate a frequency map for string "s"
	sMap := make(map[rune]int)
	for _, char := range s {
		// If the key doesn't exist,
		// it will be initialized to 0 (zero-value for an int), and then incremented
		// Otherwise, it will be incremented
		sMap[char]++
	}

	// Create & Populate a frequency map for string "t"
	tMap := make(map[rune]int)
	for _, char := range t {
		tMap[char]++
	}

	// Compare values in maps and make sure counts and chars are the same
	for sKey, sValue := range sMap {
		tValue, ok := tMap[sKey]
		if !ok || sValue != tValue {
			return false
		}
	}

	return true
}

// Sorting Strings
func IsAnagram2(s, t string) bool {

	// Edge Case: Strings aren't same length
	if len(s) != len(t) {
		return false
	}

	// Convert strings to slices of characters
	// a rune represents a Unicode code point
	sSlice := []rune(s)
	tSlice := []rune(t)

	// Define an anonymous function to sort the slices
	// NOTE: In Go, slices are passed by reference, so this function will modify the original slices.
	// The dereferencing operator (*) is not needed when working with slices.
	sortRunes := func(r []rune) {
		sort.Slice(r, func(i, j int) bool {
			return r[i] < r[j]
		})
	}

	// Sort the slices
	sortRunes(sSlice)
	sortRunes(tSlice)

	// Convert the sorted rune slices back to strings
	sSorted := string(sSlice)
	tSorted := string(tSlice)

	// Compare the sorted strings
	// If they are the same, then they are anagrams
	return sSorted == tSorted
}

// Sorting Strings (using strings package)
// https://leetcode.com/problems/valid-anagram/solutions/4410240/three-lines-of-code-by-prodonik-java-c-python-go-js-ruby-c/
// NOTE: This approach is slower than the previous approach because it uses the strings package
func IsAnagram3(s, t string) bool {
	// Convert strings to sorted slices of characters
	ss := strings.Split(s, "")
	tt := strings.Split(t, "")
	sort.Strings(ss)
	sort.Strings(tt)

	// Check if the sorted slices are equal
	return strings.Join(ss, "") == strings.Join(tt, "")
}
