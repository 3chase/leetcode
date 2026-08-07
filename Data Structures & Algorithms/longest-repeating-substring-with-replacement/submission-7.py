class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        maxw = 0

        left = 0
        right = 0
        max_freq = 0
        maxw = 0
        
        while right < len(s):
            current = s[right]
            window[current] = window.get(current, 0) + 1

            max_freq = max(max_freq, window[current])
            while (right - left + 1) > k + max_freq:     
                window[s[left]] = window[s[left]] - 1
                left += 1
            

            maxw = max(right - left + 1, maxw)
            right += 1
        return maxw




