class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while True:
            while not s[start].isalnum():
                start +=1
                if start >= end:
                  break
            while not s[end].isalnum():
                end -=1
                if start >= end:
                  break
            if start >= end:
              break
            st = s[start].lower()
            e = s[end].lower()

            if  st!=e :
                return False
            start +=1
            end -=1
        return True
      


