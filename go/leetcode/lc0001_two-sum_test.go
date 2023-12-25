package leetcode

import (
	"reflect"
	"testing"
)

// Define the type for the function under test
type functionUnderTest func([]int, int) []int

func testHelper(t *testing.T, fn functionUnderTest) {

	// Define test table w/ test cases (A slice of structs)
	tests := []struct {
		nums     []int
		target   int
		expected []int
	}{
		{[]int{2, 7, 11, 15}, 9, []int{0, 1}},
		{[]int{3, 2, 4}, 6, []int{1, 2}},
		{[]int{3, 3}, 6, []int{0, 1}},
		{[]int{-1, -2, -3, -4, -5}, -8, []int{2, 4}},
	}
	// Iterate over test cases
	// tt is a common abbrev. for "test table"
	for _, tt := range tests {
		// Call the function
		got := fn(tt.nums, tt.target)

		// Check if the result matches the expected output
		if !reflect.DeepEqual(got, tt.expected) {
			t.Errorf("%v(%v, %v) = %v; expected %v", fn, tt.nums, tt.target, got, tt.expected)
		}

	}
}

// TestTwoSum1 tests twoSum1 function via the helper method
func TestTwoSum1(t *testing.T) {
	testHelper(t, twoSum1)
}

// TestTwoSum2 tests twoSum2 function via the helper method
func TestTwoSum2(t *testing.T) {
	testHelper(t, twoSum2)
}

// TestTwoSum3 tests twoSum3 function via the helper method
func TestTwoSum3(t *testing.T) {
	testHelper(t, twoSum3)
}
