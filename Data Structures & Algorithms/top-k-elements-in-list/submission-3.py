class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        if n <= 1:
            return nums
        
        answer = []
        hm = {}
        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        buckets = [[] for _ in range(n+1)]

        for key, val in hm.items():
            buckets[val].append(key)
        
        for i in range(n, -1, -1):
            if len(answer) >= k:
                return answer
            if buckets[i]:
                for num in buckets[i]:
                    if len(answer) >= k:
                        return answer
                    answer.append(num)
        return answer






    