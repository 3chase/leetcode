class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictn = {}
        for i in range(len(nums)):    
            if nums[i] in dictn:
                return [dictn[nums[i]], i]
            dictn[target - nums[i]] = i
        return [0, 0] 
        