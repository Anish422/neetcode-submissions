class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(': ')', '{': '}', '[':']'}
       
        stack = []
        for i in range(len(s)):
            if s[i] in pairs:
                stack.append(s[i])
            elif not stack or s[i] != pairs[stack.pop()]:
                
                return False
        return not stack
            