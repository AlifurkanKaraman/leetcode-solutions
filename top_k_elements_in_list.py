# Problem: LeetCode 347 - Top K Frequent Elements
# Solution: Bucket Sort
# Time Complexity: O(N)
# Space Complexity: O(N)

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = dict()
        for i in range(len(nums)):
            if nums[i] in freq_map:
                freq_map[nums[i]] += 1
            else:
                freq_map[nums[i]] = 1
            
        buckets = [[] for _ in range(len(nums) + 1)]

        for number, count in freq_map.items():
            buckets[count].append(number)

        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result


if __name__ == "__main__":
    solution = Solution()
    input_strs = [1,2,2,3,3,3]
    k = 2
    result = solution.topKFrequent(input_strs, k)
    
    print("Input:", input_strs)
    print("Output:", result)