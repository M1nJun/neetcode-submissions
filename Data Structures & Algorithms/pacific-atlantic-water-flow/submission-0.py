class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,COLS = len(heights),len(heights[0])
        pac,atl = set(),set()
        result = []

        def dfs(r,c,visit,prevHeight):
            if (0 > r or ROWS <= r or 0 > c or COLS <= c or (r,c) in visit or prevHeight > heights[r][c]):
                return
            visit.add((r,c))

            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                dfs(nr,nc,visit,heights[r][c])
            

        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])
        
        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])

        return result