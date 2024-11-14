from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid)==0:
            return 0
        
        visited=set()
        queue=deque()
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in visited:
                    continue
                if grid[i][j]=='1':
                    queue.append((i,j))
                    count+=1
                    while queue:
                        x,y=queue.popleft()
                        for (dx,dy) in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
                            if dx>=0 and dx<len(grid) and dy>=0 and dy<len(grid[0]) and (dx,dy) not in visited:
                                if grid[dx][dy]=='1':
                                    queue.append((dx,dy))
                                    visited.add((dx,dy))
        return count   