# Two Sum

## Problem Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

## Examples

**Example 1:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Constraints

- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

## Approach

To solve this problem efficiently, we can use a hash table to store the previously visited numbers and their indices. We iterate through the array, and for each number, we check if the difference between the target and the current number is already in the hash table. If it is, we have found the two numbers that add up to the target. If not, we add the current number and its index to the hash table and continue to the next number.

This approach has a time complexity of O(n) since we iterate through the array only once, and the lookup in the hash table has an average time complexity of O(1).

## Implementation

The solution is implemented in Python using a class named `Solution` with a method `twoSum` that takes in the `nums` array and the `target` as input and returns the indices of the two numbers that add up to the target.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        
        return []  # Return an empty list if no solution is found
```

## Conclusion

The "Two Sum" problem can be efficiently solved using a hash table to store previously visited numbers. This approach allows us to find the two numbers that add up to the target in a single pass through the array, resulting in a time complexity of O(n).
