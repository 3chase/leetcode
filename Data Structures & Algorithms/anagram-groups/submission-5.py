class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmp = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for let in word:
                count[ord(let) - ord('a')] += 1
            key = tuple(count)

            hmp[key].append(word)
        return list(hmp.values())