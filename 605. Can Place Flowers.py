class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        new_array = []
        counter = 0
        if n ==0:
            return True
        if len(flowerbed) == 1:
            if flowerbed[0] ==0 and n ==1:
                return True
            return False

        if flowerbed[1] ==0 and flowerbed[0]==0:
            counter +=1
            new_array.append(1)
        else:
            new_array.append(flowerbed[0])

        for x in range(1,len(flowerbed)-1):
            if new_array[x-1] == 0 and flowerbed[x+1]==0 and flowerbed[x] != 1:
                counter +=1
                new_array.append(1)
            else:
                new_array.append(flowerbed[x])
        
        if new_array[-1] == 0 and flowerbed[-1] ==0:
            counter +=1
            new_array.append(1)
        else:
            new_array.append(flowerbed[-1])
        
        if counter >= n:
            return True
        return False
