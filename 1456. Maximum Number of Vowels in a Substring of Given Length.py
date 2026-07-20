class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l_pointer = 0
        r_pointer = k 
        sub = s[:k]
        counter = 0
        for l in sub:
            if l in ['a','e','i','o','u']:
                counter +=1
        max_c = counter
        for i in range(r_pointer,len(s)):
            if s[l_pointer] in ['a','e','i','o','u']:
                counter -=1
            l_pointer +=1
            if s[r_pointer] in ['a','e','i','o','u']:
                counter +=1
            r_pointer +=1
            if counter >= max_c:
                max_c = counter
        return max_c