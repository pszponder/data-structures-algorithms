"""
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
Build up a map of the numbers and their counts.
Compare the counts and if their values are the same, then we have an anagram.

Time Complexity: O(n)
- Iterate through the string once to build the map
- Iterate through the string again to compare the map values
- O(n) + O(n) = O(2n) = O(n)

Space Complexity: O(n)
- We create a map to store the characters and their counts
- The map will be the same size as the input string

-------------------
Approach 2: Sorting
-------------------
Sort the strings and compare them. If they are the same, return true.

Time Complexity: O(n log n)
- Sorting takes O(n log n) time
- Comparing the strings takes O(n) time
- O(n log n) + O(n) = O(n log n)

Space Complexity: O(n)
- Create two new strings that are the same size as the input strings
- O(n) + O(n) = O(2n) = O(n)
"""


def is_anagram1(s: str, t: str) -> bool:
    """Approach 1: Using Map"""

    # Edge Case: If the strings are different lengths, they are not anagrams
    if len(s) != len(t):
        return False

    # Create mapping of characters & their counts for string "s"
    s_map: dict[str, int] = {}
    for char in s:
        if char not in s_map:
            s_map[char] = 1
        else:
            s_map[char] += 1

    # Create mapping of characters & their counts for string "t"
    t_map: dict[str, int] = {}
    for char in t:
        if char not in t_map:
            t_map[char] = 1
        else:
            t_map[char] += 1

    # Compare maps
    for key, val in s_map.items():
        # Check if key is not in t_map or if the value is not the same
        if key not in t_map or t_map[key] != val:
            return False

    return True


def is_anagram2(s: str, t: str) -> bool:
    """Approach 2: Sorting"""

    # Edge case: If the strings are different lengths, they are not anagrams
    if len(s) != len(t):
        return False

    # sorted returns an array of sorted chars for the input string
    # use the join method to combine characters back to strings
    s_sorted = "".join(sorted(s))
    t_sorted = "".join(sorted(t))

    # If the strings are the same,
    # then they are anagrams
    if s_sorted == t_sorted:
        return True
    else:
        return False
