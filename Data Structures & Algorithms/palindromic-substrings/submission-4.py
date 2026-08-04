class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand(left, right):
            palidromes = 0

            while(
                left >= 0 and
                right < len(s) and
                s[left] == s[right]
            ):
                palidromes += 1
                left -= 1
                right += 1
            return palidromes

        for center in range(len(s)):
            count += expand(center, center + 1)
            count += expand(center, center)
        return count
            
                
