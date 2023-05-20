# Проходим по всем клеткам, если встречаем единицу, запускаем DFS и закрашиваем весь остров

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n, m = len(grid), len(grid[0])
        result = 0

        def dfs(i, j):
            grid[i][j] = "#"
            for x, y in neighbors:
                new_x = i + x
                new_y = j + y
                if new_x >= 0 and new_x < n and new_y >= 0 and new_y < m:
                    if grid[new_x][new_y] == "1":
                        dfs(new_x, new_y)
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    result += 1
        return result