class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastOccurence = {}
        l = 0
        length = 0
        for i, letter in enumerate(s):
            if letter in lastOccurence:
                l = max(l, lastOccurence[letter] + 1)
            lastOccurence[letter] = i
            length = max(length, i - l + 1)
        return length

        