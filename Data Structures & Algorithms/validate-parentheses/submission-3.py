class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for l in s:
            if l in ['(', '{', '[']:
                stack.append(l)
            elif l == ')':
                if len(stack) == 0:
                    return False
                if stack[-1] != '(': 
                    return False
                stack.pop()
                
            elif l == ']':
                if len(stack) == 0:
                    return False
                if stack[-1] != '[': 
                    return False
                stack.pop()
            elif l == '}':
                if len(stack) == 0:
                    return False
                if stack[-1] != '{': 
                    return False
                stack.pop()
        return len(stack) == 0
     
