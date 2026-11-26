class Solution:
    """
    Understand: 
    Input: a 2d grid
    Output: an int
    Edge cases: if impossible return -1

    Match: bfs

    Plan:

    count = 0
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    rotten = []
    fresh = 0


    for i in range (len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                rotten.append((i,j))
            elif grid[i][j] == 1:
                fresh += 1
    queue = deque(rotten)

    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            cr,cc = queue.popleft()
            neighbors = []

            for dr, dc in directions:
                nr = cr + dr
                nc = cc + dc
                if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                queue.append((nr,nc))
            count += 1 
    return count if fresh == 0 else -1
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rotten = []
        fresh = 0


        for i in range (len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        queue = deque(rotten)

        while queue:
            level_size = len(queue)
            temp = fresh
            for _ in range(level_size):
                cr,cc = queue.popleft()
                neighbors = []

                for dr, dc in directions:
                    nr = cr + dr
                    nc = cc + dc
                    if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]):
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh -= 1
                            queue.append((nr,nc))
            if temp > fresh:
                count += 1 
        return count if fresh == 0 else -1
        