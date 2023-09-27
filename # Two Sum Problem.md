# Two Sum Problem

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`. We may assume that each input would have exactly one solution, and may not use the same element twice.
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]  // nums[0] + nums[1] == 9, 2 + 7 == 9
I use a dictionary prevMap to store the elements of the nums array as we iterate through it. For each element n, we calculate the difference diff between the target and n. If diff is found in prevMap, we return the indices of diff and n. Otherwise, we store n and its index in prevMap and continue to the next element.

This solution has a time complexity of O(n) where n is the number of elements in the nums array, and a space complexity of O(n) due to the additional space required for the prevMap dictionary
```