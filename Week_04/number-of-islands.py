class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def Dfs(i,j):
            if i == 0 or j == 0 or i == x-1 or j == y-1 or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            Dfs(i-1,j)
            Dfs(i+1,j)
            Dfs(i,j-1)
            Dfs(i,j+1)
        #行数+2
        x = len(grid)+2
        y = len(grid[0])+2
        grid = [["0"]*x]+[["0"]+i+["0"] for i in grid]+[["0"]*x]
        ret = 0
        for i in range(1,x-1):
            for j in range(1,y-1):
                if grid[i][j] == "1":
                    Dfs(i,j)
                    ret += 1

        return ret