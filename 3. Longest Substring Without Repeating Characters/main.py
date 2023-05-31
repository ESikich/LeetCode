from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length, curr_length, last = 0, 0, defaultdict(lambda: -1)

        for i, char in enumerate(s):
            prev_index = last[char]

            # If the character is repeated within the current substring
            if prev_index >= 0 and i - curr_length <= prev_index:
                curr_length = i - prev_index
            else:
                curr_length += 1
            
            # Update the last seen index of the character
            last[char] = i

            # Update the maximum length if necessary
            max_length = max(max_length, curr_length)
        
        return max_length
