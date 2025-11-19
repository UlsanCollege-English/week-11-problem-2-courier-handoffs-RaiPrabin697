from collections import deque

def bfs_path(graph, s, t):
    """Return a shortest path (fewest edges) from s to t as a list of nodes.

    If s == t, return [s]. 
    If s or t not in graph, return None.
    """

    # 1) Edge cases
    if s not in graph or t not in graph:
        return None
    if s == t:
        return [s]

    # 2) Standard BFS setup
    queue = deque([s])
    visited = set([s])
    parent = {s: None}

    # 3) BFS loop
    while queue:
        node = queue.popleft()
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                parent[nbr] = node
                queue.append(nbr)

                if nbr == t:
                    # Reconstruct path
                    path = []
                    cur = t
                    while cur is not None:
                        path.append(cur)
                        cur = parent[cur]
                    return list(reversed(path))

    # 4) No path found
    return None