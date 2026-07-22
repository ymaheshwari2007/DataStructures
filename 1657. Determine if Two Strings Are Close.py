class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1dict = {}
        word2dict = {}
        if len(word1) != len(word2):
            return False
        
        for letter in word1:
            if letter in word1dict.keys():
                word1dict[letter] +=1
            else:
                word1dict[letter] = 1
        for letter in word2:
            if letter in word2dict.keys():
                word2dict[letter] +=1
            else:
                word2dict[letter] = 1
        
        if sorted(list(word1dict.values())) == sorted(list(word2dict.values())) and word1dict.keys() == word2dict.keys():
            return True
        return False

'''Better Sol:'''
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counts1 = Counter(word1)
        counts2 = Counter(word2)

        return (
            counts1.keys() == counts2.keys()
            and sorted(counts1.values()) == sorted(counts2.values())
        )