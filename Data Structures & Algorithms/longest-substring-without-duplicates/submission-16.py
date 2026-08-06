class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()

        left = 0
        end = 0
        maxs = 0

        while end < len(s):
            if s[end] in window:
                maxs = max(len(window), maxs)
                while(s[end] in window):
                    window.remove(s[left])
                    left += 1
            window.add(s[end])
            end += 1
            
        return max(maxs, len(window))
                
            


