class Solution:
    def isPalindrome(self, s: str) -> bool:
        e = len(s) - 1
        b = 0
        while b < e:    
            while not s[b].isalnum() and b < e:
                b += 1
            while not s[e].isalnum() and b < e:
                e -= 1
            if(s[b].lower() != s[e].lower()):
                return False
            e -= 1
            b += 1
        return True