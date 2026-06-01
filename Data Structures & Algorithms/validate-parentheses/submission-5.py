class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashtable = {")":"(","]":"[","}":"{"}
        for letter in s:
            if letter in hashtable.values():
                stack.append(letter)
            else:
                if not stack:
                    return False
                if letter not in hashtable.keys():
                    return False
                if hashtable[letter] != stack.pop():
                    return False
        return len(stack) == 0
