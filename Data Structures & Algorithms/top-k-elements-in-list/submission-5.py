class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in counts.items():
            buckets[count].append(num)
        

        results = []
        for i in range(len(buckets)-1, 0, -1):
            for n in buckets[i]:
                if(len(results) >= k):
                    return results
                if n not in results:
                    results.append(n)
        return results



        

        