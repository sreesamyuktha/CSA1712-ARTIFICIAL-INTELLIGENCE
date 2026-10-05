from heapq import heappush, heappop
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
def h(state):
    return sum(state[i] != 0 and state[i] != goal[i] for i in range(9))
def solve(start):
    pq = [(h(start), 0, start, [])]
    visited = set()
    while pq:
        f, g, state, path = heappop(pq)
        if state in visited:
            continue
        visited.add(state)
        path = path + [state]
        if state == goal:
            return path
        z = state.index(0)
        r, c = divmod(z, 3)
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                nz = nr * 3 + nc
                new = list(state)
                new[z], new[nz] = new[nz], new[z]
                new = tuple(new)
                if new not in visited:
                    heappush(pq, (g + 1 + h(new), g + 1, new, path))
    return None
start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
solution = solve(start)
for s in solution:
    print(s[0:3])
    print(s[3:6])
    print(s[6:9])
    print()