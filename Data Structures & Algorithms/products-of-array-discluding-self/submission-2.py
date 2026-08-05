class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        memo = {}
        answ = []
        for n in nums:
            if n in memo:
                answ.append(memo[n])
            else:
                temp = nums.copy()
                temp.remove(n)
                if len(temp) > 0:
                    prod = temp[0]
                    for t in range(1, len(temp)): 
                        prod *= temp[t]
                    memo[n] = prod
                    answ.append(prod)
        return answ