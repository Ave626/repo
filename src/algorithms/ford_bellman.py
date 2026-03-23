def bellman_ford(num_vertices,edges,start):
    distances = {i:float('inf') for i in range(1,num_vertices+1)}
    distances[start] = 0
    for _ in range(num_vertices -1):
        for u,v,ves in edges:
            if distances[u] != float('inf') and distances[u] + ves < distances[v]:
                distances[v] = distances[u] + ves        
        for u,v,ves in edges:
            if distances[u] != float('inf') and distances[u] + ves < distances[v]:
                return None
        return distances
    
if __name__ == "__main__":
    num_vertices = int(input("Введите количество городов: "))
    num_edges = int(input("Введите количество дорог: "))
    start_node = int(input("Введите номер стартового города: "))
    edges = []
    print("\nВводите данные о дорогах (Откуда Куда Стоимость):")
    for i in range(num_edges):
        u, v, ves = map(int, input(f"Дорога {i + 1}: ").split())
        edges.append((u, v, ves))        
    result_distances = bellman_ford(num_vertices, edges, start_node)

    print(f"\n--- Результат от города {start_node} ---")
    if result_distances is None:
        print("ОШИБКА: Обнаружен отрицательный цикл! Кратчайшего пути не существует.")
    else:
        for v in range(1, num_vertices + 1):
            dist = result_distances[v]
            if dist == float('inf'):
                print(f"До города {v} : Нет пути")
            else:
                print(f"До города {v} : {dist}")