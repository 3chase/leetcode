class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        window = set()

        left = 0
        window.add(s[0])
        end = 1
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
                
            


