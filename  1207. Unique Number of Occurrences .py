class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        for num in arr:
            if num in hashmap.keys():
                hashmap[num] +=1
            else:
                hashmap[num] = 1
        
        seen = []
        for val in hashmap.values():
            seen.append(val)

        if len(set(seen)) == len(seen):
            return True
        return False
