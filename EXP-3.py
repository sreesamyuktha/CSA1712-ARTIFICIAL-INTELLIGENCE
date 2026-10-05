from collections import deque
def water_jug():
    a, b = 0, 0
    q = deque([(a, b)])
    visited = set()
    while q:
        a, b = q.popleft()
        if (a, b) in visited:
            continue
        visited.add((a, b))
        print(a, b)
        if a == 2 or b == 2:
            print("Goal Reached")
            return
        states = [
            (4, b), (a, 3),       # Fill
            (0, b), (a, 0),       # Empty
            (a - min(a, 3-b), b + min(a, 3-b)),  # A -> B
            (a + min(b, 4-a), b - min(b, 4-a))   # B -> A
        ]
        for s in states:
            if s not in visited:
                q.append(s)
water_jug()