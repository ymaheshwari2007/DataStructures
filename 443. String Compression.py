class Solution:
    def compress(self, chars: List[str]) -> int:
        s = str(chars[0])
        counter = 1
        for i in range(1,len(chars)):
            if chars[i] == chars[i-1]:
                counter +=1
            else:
                if counter != 1:
                    s += str(counter)
                s+= chars[i]
                counter = 1
        if counter != 1:
            s += str(counter)
        chars[:] = list(s)
        return len(chars)