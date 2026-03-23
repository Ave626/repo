def dijkstra(num_veritices,edges,start):
    graph = {i: [] for i in range(1,num_veritices+ 1)}
    for u,v,ves in edges:
        graph[u].append((v,ves))
        graph[v].append((u,ves))
    distances = {i: float('inf') for i in range(1,num_veritices+1)}
    distances[start] = 0
    visited = set()

    while len(visited) < num_veritices:
        min_dist = float('inf')
        u = None
        for i in range(1,num_veritices+1):
            if i not in visited and distances[i] < min_dist:
                min_dist = distances[i]
                u = i
        if u is None:
            break
        visited.add(u)
        for v,ves in graph[u]:
            if v not in visited:
                new_dist = distances[u] + ves
                if new_dist < distances[v]:
                    distances[v] = new_dist
    return distances

if __name__ == "__main__":
    num_vertices = int(input("Введите количество деревень: "))
    num_edges = int(input("Введите количество возможных дорог: "))
    start_node = int(input("Введите номер стартовой деревни: "))
    edges = []
    print("\nВводите данные о дорогах (Деревня_А Деревня_Б Стоимость/Время):")
    for i in range(num_edges):
        u, v, ves = map(int, input(f"Дорога {i + 1}: ").split())
        edges.append((u, v, ves))
    result_distances = dijkstra(num_vertices, edges, start_node)
    for v in range(1, num_vertices + 1):
        dist = result_distances[v]
        if dist == float('inf'):
            print(f"До деревни {v} : Нет пути")
        else:
            print(f"До деревни {v} : {dist}")