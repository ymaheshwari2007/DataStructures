'''First solution counts so a bit slow'''
class RecentCounter:

    def __init__(self):
        self.arr = []
        self.start = 0
    def ping(self, t: int) -> int:
        left_range = t-3000
        right_range = t
        self.arr.append(t)
        counter = 0
        for i in range(self.start, len(self.arr)):
            if self.arr[i] >= left_range and self.arr[i] <= right_range:
                counter +=1
            else:
                self.start = i
        
        return counter


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

'''Faster approach using MATHS instead'''
class RecentCounter:

    def __init__(self):
        self.arr = []
        self.start = 0
    def ping(self, t: int) -> int:
        left_range = t-3000
        right_range = t
        self.arr.append(t)
        for i in range(self.start, len(self.arr)):
            if self.arr[i] < left_range or self.arr[i] > right_range:
                self.start +=1
            else:
                break
        return len(self.arr) - self.start


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)