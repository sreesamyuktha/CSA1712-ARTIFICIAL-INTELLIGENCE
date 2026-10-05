from collections import deque
def valid(m, c):
    return (m == 0 or m >= c) and (3-m == 0 or 3-m >= 3-c)
def solve():
    start = (3, 3, 0, 0)   # M, C, boat, 0=left
    q = deque([(start, [start])])
    visited = {start}
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    while q:
        state, path = q.popleft()
        m, c, b, side = state
        if state == (0, 0, 1, 1):
            for x in path:
                print(x)
            return
        for dm, dc in moves:
            nm = m - dm if side == 0 else m + dm
            nc = c - dc if side == 0 else c + dc
            nb = 1 - side
            if 0 <= nm <= 3 and 0 <= nc <= 3 and valid(nm, nc):
                new = (nm, nc, nb, nb)
                if new not in visited:
                    visited.add(new)
                    q.append((new, path + [new]))
solve()