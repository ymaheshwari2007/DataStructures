def pivotIndex( nums: list[int]) -> int:
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(nums[i] + prefix[i])
        
        sum = prefix[-1]
        
        suffix = []
        for i in range(len(prefix)):
          suffix.append(sum-prefix[i])
          
        
        print(prefix)
        print(suffix)

        # left = 0
        # right = lens(prefix)
        
        # for i in range(len)
        
        for i in range(len(prefix)-1):
          if prefix[i] == suffix[i+1]:
            return i
        
        return -1
            