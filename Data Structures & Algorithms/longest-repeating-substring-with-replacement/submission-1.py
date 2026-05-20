class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_number = 0
        res = 0
        count = {}
        for r, letter in enumerate(s):
            count[letter] = 1 + count.get(letter, 0)
            max_number = max(max_number, count[letter])
            while max_number < r-l+1-k:
                count[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res


            