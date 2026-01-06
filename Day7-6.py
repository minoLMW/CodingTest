# 문제 - 알고리즘 (BFS / 결자)
# 다음과 같은 0/1 격자가 주어진다.
# 1인 칸만 이동 가능하며, 상/하/좌/우로만 이동할 수 있다.
# 좌상단 (0,0)에ㅓㅅ 우하단 (n-1,m-1)까지 최단 이동 칸 수를 구하시오.
# 이동할 수 없다면 -1을 반환하시오.

grid = [
    [1,1,0],
    [1,1,0],
    [0,1,1]
]

q = deque()
q.append((0, 0))
dist[0][0] = 1

while q:
    x, y = q.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
