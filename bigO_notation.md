# Big-O Notation

## What is Big-O Notation?

`Big-O Notation` is a way to express the `time` and `space` efficiency of an algorithm by analyzing the amount of time and space an algorithm takes / consumes as the input size to the algorithm grows to infinity.

In `Big-O Notation`, the efficiency of an algorithm is expressed in terms of the worst-case scenario and represented by `O(f(n))` where `f(n)` is a function describing how fast the algorithm's `time` and `space` requirements increase as the size of the input data `n` increases.

## Time Complexity

`Time Complexity` describes how the runtime of an algorithm increases as the input size grows.

Ex. an algorithm w/ linear time complexity `O(n)` means that the runtime increases linearly w/ the size of the input

## Space Complexity

`Space Complexity` describes how the space (memory) required by an algorithm changes as the input size grows.

Ex. an algorithm w/ linear time complexity `O(n)` means that the space needed increases linearly w/ the input size.

## Common Big-O Complexities (from Best to Worst)

### Summary

```txt
O(1)        Constant
O(log n)    Logarithmic
O(n)        Linear
O(n log n)  Linearithmic
O(n^2)      Quadratic
O(n * m)    Quadratic
O(n^m)      Polynomial
O(2^n)      Exponential
```

### O(1) -- Constant

Algorithm's runtime / space requirements are constant, regardless of the input size.

```python
"""
Arrays / Lists

O(1) operations for arrays include:
- inserting from end
- removing from end
- lookup by index (regardless of list's size)
"""
nums = [1, 2, 3]
nums.append(4)    # push to end
nums.pop()        # pop from end
nums[0]           # lookup by index
nums[1]           # lookup by index
nums[2]           # lookup by index


"""
HashMap / Set

O(1) operations for HashMaps / Sets / Dictionaries include:
- inserting
- removing
- lookup
"""
hashMap = {}
hashMap["key"] = 10     # insert
print("key" in hashMap) # lookup
print(hashMap["key"])   # lookup
hashMap.pop("key")      # remove
```

### O(log n) -- Logarithmic

Common in algorithms that divide the problem in half at each step, like binary search

```python
# Binary search
nums = [1, 2, 3, 4, 5]
target = 6
l, r = 0, len(nums) - 1
while l <= r:
    m = (l + r) // 2
    if target < nums[m]:
        r = m - 1
    elif target > nums[m]:
        l = m + 1
    else:
        print(m)
        break

# Binary Search on BST
def search(root, target):
    if not root:
        return False
    if target < root.val:
        return search(root.left, target)
    elif target > root.val:
        return search(root.right, target)
    else:
        return True
```

### O(n) -- Linear

Runtime / space requirements grow linearly w/ the input size

**NOTE:** When traversing through the elements of an array / list, each time you traverse it, you traverse it at `O(n)`
- Ex. if you traverse an array 3 times, the time complexity is `O(3n)` or `O(n)` since constants are dropped in `Big-O` notation.

```python
"""
Common O(n) Operations:
- Summing the values of an array / list
- A loop (eg. looping through each element in an array / list)
- Inserting into the middle of an array / list
- Removing from the middle of an array / list
- Searching for a value in an array / list
- Building a heap

While a doubly nested loop is typically O(n^2),
it can be optimized to be O(n)
ex. monotonic stack / sliding window
"""

nums = [1, 2, 3]
sum(nums)           # sum of array
for n in nums:      # looping
    print(n)

nums.insert(1, 100) # insert from middle of array / list
nums.remove(100)    # remove from middle of array / list
print(100 in nums)  # search an array / list

import heapq
heapq.heapify(nums) # build heap
```

### O(n log n) -- Linearithmic

Common in efficient sorting algorithms like merge sort and heap sort

**NOTE:** Most built-in sorting methods are typically `O(n log n)`

`Merge Sort`

```python
def merge_sort(lst):
    # Sorting a list using merge sort
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

`Heap Sort`

```python
def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

# Example usage:
unsorted_list = [12, 11, 13, 5, 6, 7]
print("Unsorted array:", unsorted_list)

heap_sort(unsorted_list)

print("Sorted array:", unsorted_list)
```

### O(n^2) -- Quadratic

Runtime / space requirements grow w/ the square of the input size

```python
# Doubly nested loops are generally O(n^2)
def quadratic_operation(lst):
    # Nested loops iterating through each pair of elements in the list
    for i in lst:
        for j in lst:
            print(i, j)


# Traverse a square grid
nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(nums)):
    for j in range(len(nums[i])):
        print(nums[i][j])


# Get every pair of elements in array
nums = [1, 2, 3]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        print(nums[i], nums[j])


# Insertion sort (insert in middle n times -> n^2)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
```

### O(n * m) -- Quadratic

`O(n * m)` is also quadratic where `n` and `m` represent different input sizes or dimensions.

`O(n * m)` is equivalent to `O(n^2)` when the size of `n` and `m` are the same.

```python
# Get every pair of elements from two arrays
nums1, nums2 = [1, 2, 3], [4, 5]
for i in range(len(nums1)):
    for j in range(len(nums2)):
        print(nums1[i], nums2[j])

# Traverse rectangle grid
# This is O(n^2) but more generally, O(n * m)
nums = [[1, 2, 3], [4, 5, 6]]
for i in range(len(nums)):
    for j in range(len(nums[i])):
        print(nums[i][j])
```

### O(n^m) -- Polynomial

`O(n^m)` includes `O(n)`, `O(n^2)`, `O(n * m)`, `O(n^3)`, etc.

The higher the value of `m`, the larger the time and space complexity.
- `m = 1` -- `O(n)`, linear
- `m = 2` -- `O(n^2)`, quadratic
- `m = 3` -- `O(n^3)`, cubic
- `m = 4` -- `O(n^4)`, quartic
- etc.

```python
# Get every triplet of elements in array
nums = [1, 2, 3]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            print(nums[i], nums[j], nums[k])
```

### O(2^n) -- Exponential

Often seen in algorithms w/ recursive solutions that solve a problem of size `n` by recursively solving two smaller problems

```python
def fibonacci_recursive(n):
    # Calculating the nth Fibonacci number using a recursive approach
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
```


## Resources / References

- [Neetcode.io - Big O Notation](https://neetcode.io/courses/lessons/big-o-notation)
- [freeCodeCamp - Big O Notation - Full Course](https://www.youtube.com/watch?v=Mo4vesaut8g)
- [Fireship - Big-O Notation in 100 Seconds](https://www.youtube.com/watch?v=g2o22C3CRfU)