class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        answ = []
        
        for i in range(0, len(snums)-1):
            k = i
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
                    if [snums[i], snums[j], snums[k]] not in answ:
                        answ.append([snums[i], snums[j], snums[k]])
                    j -= 1
        return answ



