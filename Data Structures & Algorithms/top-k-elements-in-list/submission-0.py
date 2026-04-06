class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        most_common = counts.most_common(k)

        res = [x[0] for x in most_common]

        return res 
