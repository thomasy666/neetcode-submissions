class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for string in strs:
            key = [0] * 26
            for letter in string:
                key[ord(letter) - ord("a")] += 1
            freq[tuple(key)].append(string)
        return list(freq.values()) 