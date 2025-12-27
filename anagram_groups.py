from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for s in strs:
            count = [0] * 26

            for char in s:
                index = ord(char) - ord('a')
                count[index] += 1
            
            key = tuple(count)

            if key not in anagram_map:
                anagram_map[key] = []
            
            anagram_map[key].append(s)

        return list(anagram_map.values())

if __name__ == "__main__":
    solution = Solution()
    input_strs = ["act","pots","tops","cat","stop","hat"]
    result = solution.groupAnagrams(input_strs)
    
    print("Input:", input_strs)
    print("Output:", result)