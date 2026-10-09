from itertools import permutations
dist = [[0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]]
n = len(dist)
best = float('inf')
path = None
for p in permutations(range(1, n)):
    route = (0,) + p + (0,)
    cost = sum(dist[route[i]][route[i+1]] for i in range(n))
    if cost < best:
        best = cost
        path = route
print("Minimum Cost:", best)
print("Best Path:", " -> ".join(str(x) for x in path))