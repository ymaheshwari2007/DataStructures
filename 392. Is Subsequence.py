class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer2 = 0
        lenT = len(t)
        for letter in s:
            found = False
            for i in range(pointer2,lenT):
                if t[i] == letter:
                    found = True
                    pointer2 +=1
                    break
                pointer2 +=1
            if not found:
                return False
        return True

