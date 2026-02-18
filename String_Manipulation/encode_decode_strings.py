# Problem: LeetCode 271 - Encode and Decode Strings
# Solution: Length-Prefixed Delimiter (String Manipulation)
# Time Complexity: O(N)
# Space Complexity: O(N)

from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        sentence = ""
        for s in strs:
            sentence += str(len(s)) + '#' + s

        return sentence
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length

        return res

Solution = Solution()

input = ["hello", "world"]
print(Solution.encode(input))
input2 = "5#hello5#world"
print(Solution.decode(input2))