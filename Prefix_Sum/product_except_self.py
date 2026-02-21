# Problem: LeetCode 238 - Product of Array Except Self
# Solution: Prefix and Suffix Arrays
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_size = len(nums)
        result = [1] * nums_size
        prefix = [1] * nums_size
        suffix = [1] * nums_size
        
        for i in range(1, nums_size):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            
        for i in range(nums_size - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        for i in range(nums_size):
            result[i] = prefix[i] * suffix[i]
        
        return result

if __name__ == "__main__":
    solution = Solution()
    input = [1, 2, 4, 6]
    result = solution.productExceptSelf(input)
    
    print("Input:", input)
    print("Output:", result)