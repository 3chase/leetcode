class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmp = {}
        sol = []
        counter = 0
        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char)-ord('a')] = key[ord(char)-ord('a')] + 1
            
            key = tuple(key)
            if key in hmp:
                sol[hmp[key]].append(word)
            else:
                sol.append([word])
                hmp[key] = counter
                counter += 1
        return sol

             
