import sys
sys.setrecursionlimit(10**7)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]


dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1),  (1, 0), (1, 1)
]

def in_bounds(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y, height):
    stack = [(x, y)]
    cells = []
    visited[x][y] = True
    while stack:
        cx, cy = stack.pop()
        cells.append((cx, cy))
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if in_bounds(nx, ny) and not visited[nx][ny] and grid[nx][ny] == height:
                visited[nx][ny] = True
                stack.append((nx, ny))
    return cells

peaks = 0
valleys = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cells = dfs(i, j, grid[i][j])
            h = grid[i][j]
            is_peak = True
            is_valley = True

            for (cx, cy) in cells:
                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy
                    if in_bounds(nx, ny):
                        nh = grid[nx][ny]
                        if nh != h:
                            if nh > h:
                                is_peak = False
                            if nh < h:
                                is_valley = False
            if is_peak:
                peaks += 1
            if is_valley:
                valleys += 1

print(peaks, valleys)
