# Longest Substring Without Repeating Characters

## Problem Description

Given a string, find the length of the longest substring without repeating characters.

### Example

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. Notice that the answer must be a substring; "pwke" is a subsequence and not a substring.

### Approach

To solve this problem, we can use the "sliding window" technique with a few optimizations:

1. We maintain a sliding window that starts from the left and expands to the right until we encounter a repeating character.
2. We use a dictionary (or an array) to keep track of the last seen index of each character within the window.
3. When we encounter a repeating character, we update the start index of the window to skip the repeated character and continue searching for a longer substring.
4. We keep track of the maximum length of the substring as we iterate through the string.

By using the sliding window approach, we can efficiently find the length of the longest substring without repeating characters in a single pass through the string.

### Time Complexity

The time complexity of this solution is O(n), where n is the length of the input string. This is because we iterate through the string once, updating the window boundaries and maintaining the last seen index of each character.

### Space Complexity

The space complexity is O(1) or O(k), depending on the size of the character set. In this solution, we use a dictionary (or an array) to store the last seen index of each character, which requires O(k) space, where k is the size of the character set. However, since the constraints specify that the input consists of English letters, digits, symbols, and spaces, the character set is limited and constant.

### Optimization

We can further optimize the solution by using an array instead of a dictionary to store the last seen index of each character. This eliminates the overhead of hash map operations and improves performance. Additionally, we can apply early termination when the maximum possible length is reached, and utilize a fixed-size array instead of a dynamic data structure for character frequencies.
