class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        answ = []
        
        for i in range(0, len(snums)-1):
            if i > 0 and snums[i] == snums[i-1]:
                continue
            k = i+1
            j = len(snums)-1
            while(k < j):
                target = -snums[i]
                if (k == i):
                    k += 1
                if (j == i):
                    j -= 1
                if target > (snums[j] + snums[k]):
                    k += 1
                elif target < (snums[j] + snums[k]):
                    j -= 1
                elif target == (snums[j] + snums[k]):
                    answ.append([snums[i], snums[k], snums[j]])
                    k += 1
                    j -= 1
                    while k < j and snums[j] == snums[j+1]:
                        j -= 1
                    while k < j and snums[k] == snums[k-1]:
                        k += 1
        return answ



