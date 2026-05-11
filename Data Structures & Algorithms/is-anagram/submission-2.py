class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letterss = {}
        letterst = {}
        for letter in s:
            letterss[letter] = letterss.get(letter, 0) + 1
        letterst = {}
        for letter in t:
            letterst[letter] = letterst.get(letter, 0) + 1
        return letterss == letterst
        