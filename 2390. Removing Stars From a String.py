class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for l in s:
            if l == '*':
                stack.pop()
            else:
                stack.append(l)
        return "".join(stack)