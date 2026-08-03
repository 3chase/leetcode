

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}

        for word in strs:
            key = [0] * 26
            for let in word:
                key[ord(let) - ord('a')] += 1
            
            word_dict.setdefault(tuple(key), []).append(word)
        return list(word_dict.values())

        

            
                

