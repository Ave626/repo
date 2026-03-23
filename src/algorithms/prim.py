def prim(num_veritices,edges):
    visited = {1}
    answer = []
    total = 0
    while len(visited) < num_veritices:
        edge = None
        min_ves = float('inf')
        for u,v,ves in edges:
            if (u in visited and v not in visited) or (v in visited and u not in visited):
                if ves < min_ves:
                    min_ves = ves
                    edge = (u,v,ves)
        if edge is None:
            return 0
        
        u,v,ves = edge
        answer.append(edge)
        total += ves
        visited.add(u)
        visited.add(v)
    return answer,total


if __name__ == "__main__":
    num_vertices = int(input("Введите количество деревень: "))
    num_edges = int(input("Введите количество возможных дорог: "))
    edges = []
    print("\nВводите данные о дорогах (Деревня_А Деревня_Б Стоимость):")
    for i in range(num_edges):
        u, v, ves = map(int, input(f"Дорога {i + 1}: ").split())
        edges.append((u, v, ves))
        
    answer, cost = prim(num_vertices, edges)
    print("\n--- Результат ---")
    if answer:
        print("Построенные дороги:")
        for u, v, w in answer:
            print(f"{u} - {v} : {w}")
        print(f"Общая стоимость: {cost}")
    else:
        print("Ошибка: граф несвязный или введено недостаточно дорог!")