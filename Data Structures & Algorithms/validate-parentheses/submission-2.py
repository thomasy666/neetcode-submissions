class Solution:
    def isValid(self, s: str) -> bool:
        li = []
        closetoopen = {"]" : "[", ")" : "(", "}" : "{" }
        for l in s:
            if l in closetoopen:
                if li and closetoopen[l] == li[-1]:
                    li.pop()
                else:
                    return False
            else:
                li.append(l)
        if li:
            return False
        return True