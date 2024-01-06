"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/description/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

===========
APPROACHES:
===========

----------------------
Approach 1: 2-Pointers
----------------------
- Add 2 pointers on either end of the string
- If the values of the pointers are the same,
  move the pointers towards each other
- Keep checking if the pointers point to the same value
- If the values don't equal at any step,
  then you don't have a palindrome
- If after the pointers cross, you have a palindrome

Time Complexity: O(n)
- If string is n long, it takes n/2 times to traverse the string from both ends
- O(n/2) = O(n)
- Cleaning a string to remove characters is also O(n)

Space Complexity: O(n)
- Building a New String

-------------------------
Approach 2: String Slices
-------------------------

Time Complexity: O(n)
- Same as Solution 1

Space Complexity: O(n)
- Same as Solution 1

----------------------------------
Approach 3: 2-Pointers (Optimized)
----------------------------------
Same as Approach # 1 but with optimization
to avoid building a new string

- Add 2 pointers on either end of the string
- If the values of the pointers are the same,
  move the pointers towards each other
- Keep checking if the pointers point to the same value
- If the values don't equal at any step,
  then you don't have a palindrome
- If after the pointers cross, you have a palindrome

Time Complexity: O(n)
- If string is n long, it takes n/2 times to traverse the string from both ends
- O(n/2) = O(n)

Space Complexity: O(1)
- No new string is created
"""


def is_palindrome1(s: str) -> bool:
    """2-Pointers Approach"""

    # Use list comprehension to filter out non-alphanumeric characters and spaces
    # and also lower the case
    cleaned_chars = [char.lower() for char in s if char.isalnum()]

    # Join the filtered characters to form the cleaned string
    cleaned_str = "".join(cleaned_chars)

    # Edge Case: Empty String or 1-char string
    if len(cleaned_str) <= 1:
        return True

    # Define pointers and their starting indices
    lptr = 0
    rptr = len(cleaned_str) - 1

    # Keep checking until pointers cross
    while lptr < rptr:
        # If values of pointers are not equal, not palindrome
        if cleaned_str[lptr] != cleaned_str[rptr]:
            return False

        # Move pointers towards each-other
        lptr += 1
        rptr -= 1

    # Pointers have crossed, we have a palindrome
    return True


def is_palindrome2(s: str) -> bool:
    """Slice Manipulation"""

    # Build a cleaned string
    cleaned = ""
    for c in s:
        if c.isalnum():
            cleaned += c.lower()

    # Compare cleaned string to reversed cleaned string slice
    return cleaned == cleaned[::-1]


def is_palindrome3(s: str) -> bool:
    """2-Pointers Optimized"""
    # Define Pointers
    lptr, rptr = 0, len(s) - 1

    # Keep looping while pointers haven't crossed
    while lptr < rptr:
        # Skip over non-alphanumeric chars for lptr
        while lptr < rptr and not s[lptr].isalnum():
            lptr += 1

        # Skip over non-alphanumeric chars for rptr
        while rptr > lptr and not s[rptr].isalnum():
            rptr -= 1

        # If value's at pointers don't equal, not a palindrome
        if s[lptr].lower() != s[rptr].lower():
            return False

        # Update pointers
        lptr += 1
        rptr -= 1
    return True
