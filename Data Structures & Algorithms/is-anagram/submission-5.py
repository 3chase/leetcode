class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for l in s:
            dict[l] = dict.get(l, 0) + 1
        for l in t:
            dict[l] = dict.get(l, 0) - 1
        for key in dict.keys():
            if dict[key] != 0:
                return False
        return True