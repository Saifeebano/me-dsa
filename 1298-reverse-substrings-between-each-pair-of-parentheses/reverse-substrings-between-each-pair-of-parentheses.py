class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        res = []
        
        for char in s:
            if char == '(':
                # Record the index in 'res' where this '(' starts
                stack.append(len(res))
            elif char == ')':
                # Pop the matching '(' position and reverse the slice in 'res'
                start = stack.pop()
                res[start:] = res[start:][::-1]
            else:
                res.append(char)
                
        return "".join(res)