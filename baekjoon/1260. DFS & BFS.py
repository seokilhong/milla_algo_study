V, E, start = map(int, input().split())

graph = {i: set() for i in range(1, V + 1)}

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

visited = [False] * (V + 1)


def dfs(graph, vertex, visited, ans):
    ans.append(vertex)
    visited[vertex] = True
    visiting_list = sorted(list(graph[vertex]))
    for next_vertex in visiting_list:
        if visited[next_vertex] == True:
            continue
        dfs(graph, next_vertex, visited, ans)
    return ans


def bfs(graph, start):
    visited = [False] * (V + 1)
    queue = [start]
    visited[start] = True
    ans = []

    while queue:
        vertex = queue.pop(0)
        ans.append(vertex)
        visiting_list = sorted(list(graph[vertex]))
        for next_vertex in visiting_list:
            if not visited[next_vertex]:
                visited[next_vertex] = True
                queue.append(next_vertex)
    return ans


dfs_ans = dfs(graph, start, visited, [])
bfs_ans = bfs(graph, start)

for i in dfs_ans:
    print(i)
for i in bfs_ans:
    print(i)
