# -----------------------------------------megoldas-------------------------------------------
import sys

sys.setrecursionlimit(10**6)


def dfs(node, parent, adj, dp):
    dp[node][0] = 0  # Ha nem párosítjuk a node-ot
    dp[node][1] = 1  # Ha párosítjuk a node-ot (mint szülő)

    for neighbor in adj[node]:
        if neighbor == parent:
            continue

        dfs(neighbor, node, adj, dp)

        # Ha a node-ot nem párosítjuk
        dp[node][0] += max(dp[neighbor][0], dp[neighbor][1])

        # Ha a node-ot párosítjuk
        dp[node][1] += dp[neighbor][0]


def max_matching(n, edges):
    adj = [[] for _ in range(n)]
    dp = [[0, 0] for _ in range(n)]

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Kezdjük a DFS-t a 0-ás csúcsról (vagy bármely más csúcsról)
    dfs(0, -1, adj, dp)

    # A válasz a gyökér csúcs párosítás nélküli vagy párosított állapota
    return max(dp[0][0], dp[0][1])


"""
# Bemenet olvasása
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# A kimenet
print(max_matching(n, edges))
"""
# ------------------------------------------teszt----------------------------------------------
import sys

sys.setrecursionlimit(10**6)


def dfs(node, parent, adj, dp):
    dp[node][0] = 0  # Ha nem párosítjuk a node-ot
    dp[node][1] = 1  # Ha párosítjuk a node-ot (mint szülő)

    for neighbor in adj[node]:
        if neighbor == parent:
            continue

        dfs(neighbor, node, adj, dp)

        # Ha a node-ot nem párosítjuk
        dp[node][0] += max(dp[neighbor][0], dp[neighbor][1])

        # Ha a node-ot párosítjuk
        dp[node][1] += dp[neighbor][0]


def max_matching(n, edges):
    adj = [[] for _ in range(n)]
    dp = [[0, 0] for _ in range(n)]

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Kezdjük a DFS-t a 0-ás csúcsról (vagy bármely más csúcsról)
    dfs(0, -1, adj, dp)

    # A válasz a gyökér csúcs párosítás nélküli vagy párosított állapota
    return max(dp[0][0], dp[0][1])


# Teszt 1
n1 = 5
edges1 = [(0, 1), (0, 2), (2, 3), (2, 4)]
print(max_matching(n1, edges1))  # Elvárt kimenet: 2

# Teszt 2
n2 = 3
edges2 = [(0, 1), (1, 2)]
print(max_matching(n2, edges2))  # Elvárt kimenet: 1

# Teszt 3
n3 = 4
edges3 = [(0, 1), (1, 2), (2, 3)]
print(max_matching(n3, edges3))  # Elvárt kimenet: 2

# Teszt 4
n4 = 6
edges4 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 5)]
print(max_matching(n4, edges4))  # Elvárt kimenet: 3

# Teszt 5
n5 = 7
edges5 = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
print(max_matching(n5, edges5))  # Elvárt kimenet: 3

# Teszt 6
n6 = 2
edges6 = [(0, 1)]
print(max_matching(n6, edges6))  # Elvárt kimenet: 1

# Teszt 7
n7 = 8
edges7 = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 7)]
print(max_matching(n7, edges7))  # Elvárt kimenet: 4

# Teszt 8
n8 = 9
edges8 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]
print(max_matching(n8, edges8))  # Elvárt kimenet: 4

# Teszt 9
n9 = 6
edges9 = [(0, 1), (0, 2), (1, 3), (1, 4), (3, 5)]
print(max_matching(n9, edges9))  # Elvárt kimenet: 3

# Teszt 10
n10 = 10
edges10 = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7), (4, 8), (5, 9)]
print(max_matching(n10, edges10))  # Elvárt kimenet: 5
