class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if(len(nums) < 2):
            return False
        set_dupe = set()
        for n in nums:
            if n in set_dupe:
                return True
            set_dupe.add(n)
        return False


        