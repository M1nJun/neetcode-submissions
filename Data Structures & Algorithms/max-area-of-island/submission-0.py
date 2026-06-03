class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            area = 1
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr,dc in directions:
                    nr, nc = row+dr, col+dc
                    if (nr in range(ROWS) and nc in range(COLS) and
                        grid[nr][nc] == 1 and (nr,nc) not in visited):
                        q.append((nr,nc))
                        visited.add((nr,nc))
                        area += 1

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == 1:
                    currArea = bfs(r,c)
                    maxArea = max(maxArea, currArea)
        
        return maxArea
                    
