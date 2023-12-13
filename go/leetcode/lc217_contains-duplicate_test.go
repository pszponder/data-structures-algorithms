package leetcode

import (
	"testing"
)

const (
	Example1 = "Example 1"
	Example2 = "Example 2"
	Example3 = "Example 3"
	ErrorMsg = "Expected %v, but got %v"
)

func TestContainsDuplicate0(t *testing.T) {
	// tests is an array of anonymous structs
	tests := []struct {
		name     string
		input    []int
		expected bool
	}{
		{Example1, []int{1, 2, 3, 1}, true},
		{Example2, []int{1, 2, 3, 4}, false},
		{Example3, []int{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}, true},
		// Add more test cases as needed
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			result := ContainsDuplicate0(test.input)
			if result != test.expected {
				t.Errorf(ErrorMsg, test.expected, result)
			}
		})
	}
}

func TestContainsDuplicate1(t *testing.T) {
	// tests is an array of anonymous structs
	tests := []struct {
		name     string
		input    []int
		expected bool
	}{
		{Example1, []int{1, 2, 3, 1}, true},
		{Example2, []int{1, 2, 3, 4}, false},
		{Example3, []int{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}, true},
		// Add more test cases as needed
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			result := ContainsDuplicate1(test.input)
			if result != test.expected {
				t.Errorf(ErrorMsg, test.expected, result)
			}
		})
	}
}

func TestContainsDuplicate2(t *testing.T) {
	tests := []struct {
		name     string
		input    []int
		expected bool
	}{
		{Example1, []int{1, 2, 3, 1}, true},
		{Example2, []int{1, 2, 3, 4}, false},
		{Example3, []int{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}, true},
		// Add more test cases as needed
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			result := ContainsDuplicate2(test.input)
			if result != test.expected {
				t.Errorf(ErrorMsg, test.expected, result)
			}
		})
	}
}
