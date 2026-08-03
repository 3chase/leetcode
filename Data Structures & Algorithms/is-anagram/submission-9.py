class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(t) != len(s)):
            return False
        dict = {}
        for i in range(len(t)):
            dict[s[i]] = dict.get(s[i], 0) + 1
            dict[t[i]] = dict.get(t[i], 0) - 1
        for key in dict.keys():
            if dict[key] != 0:
                return False
        return True
        