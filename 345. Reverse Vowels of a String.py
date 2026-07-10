'''Solved with using a stack'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        for x in range(len(s)):
            if s[x].lower() in ['a','e','i','o','u']:
                stack.append(s[x])
        
        out = ''
        for x in range(len(s)):
            if s[x].lower() in ['a','e','i','o','u']:
                out+= stack.pop()
                stack[:-1]
            else:
                out+= s[x]
        
        return out

'''Solved with 2 pointers'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        l = list(s)

        while left <= right:
            if s[left].lower() in ['a','e','i','o','u'] and s[right].lower() in ['a','e','i','o','u']:
                temp = l[left]
                l[left] = l[right]
                l[right] = temp
                left +=1
                right -=1
            elif s[left].lower() in ['a','e','i','o','u'] and s[right].lower() not in ['a','e','i','o','u']:
                right -=1
            
            elif s[left].lower() not in ['a','e','i','o','u'] and s[right].lower()  in ['a','e','i','o','u']:
                left +=1
            
            else:
                left +=1
                right -=1

        return "".join(l)