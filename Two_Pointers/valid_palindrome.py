# Problem: LeetCode 125 - Valid Palindrome
# Solution: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        
        while i < j:
            # Move left pointer to next valid character
            while i < j and not s[i].isalnum():
                i += 1
                
            # Move right pointer to next valid character
            while i < j and not s[j].isalnum():
                j -= 1
                
            # Compare the characters (ignoring case)
            if s[i].lower() != s[j].lower():
                return False
            
            # Move both inward for the next check
            i += 1
            j -= 1
            
        return True