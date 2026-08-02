class Solution:
    def isPalindrome(self, s: str) -> bool:
        e = len(s) - 1
        b = 0
        for n in range(len(s)):    
            while not s[b].isalnum() and b < len(s)-1:
                b += 1
            while not s[e].isalnum() and e > 0:
                e -= 1
            print(f"N: {b}")
            print(f"E: {e}")
            if(b >= e):
                return True
            if(s[b].lower() != s[e].lower()):
                return False
            e -= 1
            b += 1
        return False