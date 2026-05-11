class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        res = []
        i = 0
        while (i < len(s)):
            j = i
            while (s[j] != "#"):
                j += 1
            res.append(s[j+1:j+1+int(s[i:j])])
            i = j+1+int(s[i:j])
        return res
