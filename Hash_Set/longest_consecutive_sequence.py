# Problem: LeetCode 128 - Longest Consecutive Sequence
# Solution: Hash Set
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest_streak = 0
        
        for num in hash_set:
            # Check if this is the start of a sequence
            if (num - 1) not in hash_set:
                curr_num = num
                curr_streak = 1
                
                # Count upwards as long as the next number exists
                while (curr_num + 1) in hash_set:
                    curr_num += 1
                    curr_streak += 1
                    
                # Only keep the biggest streak!
                longest_streak = max(longest_streak, curr_streak)
                
        return longest_streak