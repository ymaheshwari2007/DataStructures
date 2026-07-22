class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = {}
        count = 0
        for row in grid:
            key = tuple(row)
            if key in rows.keys():
                rows[tuple(key)] +=1
            else:
                rows[tuple(key)] = 1
        
        for x in range(len(grid)):
            col = []
            for y in range(len(grid)):
                col.append(grid[y][x])
            key = tuple(col)
            if key in rows:
                count+= rows[key]
        return count

