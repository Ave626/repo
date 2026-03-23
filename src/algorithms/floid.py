graph = [[0,124,57,float("inf"),69],
    [float("inf"),0,5,45,89],
    [45,47,0,75,float("inf")],
    [float("inf"),35,float("inf"),0,23],
    [58,12,78,89,0]]

n = len(graph)
for i in range(n):
    for j in range(n):
        for k in range(n):
            graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])

for i in range(n):
    print(graph[i])