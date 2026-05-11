class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        for n, f in frequency.items():
            freq[f].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res