class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        starts = []
        for num in numset:
            if num-1 not in numset:
                starts.append(num)

        maxseq = 0
        for start in starts:
            num = start
            seqcount = 0
            while(num in numset):
                seqcount += 1
                num += 1
            maxseq = max(maxseq, seqcount)
        return maxseq
        
