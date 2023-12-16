package leetcode

import "testing"

// isAnagramFunc defines the type for an anagram function
type isAnagramFunc func(string, string) bool

// Helper function to test an anagram function
func testIsAnagram(t *testing.T, fn isAnagramFunc) {
	// Test cases
	tests := []struct {
		s, t string
		want bool
	}{
		{"anagram", "nagaram", true},
		{"rat", "car", false},
		{"listen", "silent", true},
		{"hello", "world", false},
		{"", "", true},
		{"a", "a", true},
		{"a", "b", false},
		{"ab", "ba", true},
		{"ab", "a", false},
	}

	// Iterate over test cases
	// tt is a common abbrev. for "test table"
	for _, tt := range tests {
		// Call the function
		got := fn(tt.s, tt.t)

		// Check if the result matches the expected output
		if got != tt.want {
			t.Errorf("%v(%s, %s) = %v; want %v", fn, tt.s, tt.t, got, tt.want)
		}
	}
}

// TestIsAnagram1 tests the IsAnagram1 function
func TestIsAnagram1(t *testing.T) {
	testIsAnagram(t, IsAnagram1)
}

// TestIsAnagram2 tests the IsAnagram2 function
func TestIsAnagram2(t *testing.T) {
	testIsAnagram(t, IsAnagram2)
}

func TestIsAnagram3(t *testing.T) {
	testIsAnagram(t, IsAnagram3)
}
