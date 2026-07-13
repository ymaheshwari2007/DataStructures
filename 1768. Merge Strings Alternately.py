class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        if len(word1) > len(word2):
            w1 = True
        else:
            w1 = False
        
        if w1:
            for x in range(len(word2)):
                ans += word1[x]
                ans += word2[x]
            ans += word1[len(word2):]
        else:
            for x in range(len(word1)):
                ans += word1[x]
                ans += word2[x]
            ans += word2[len(word1):]
        return ans