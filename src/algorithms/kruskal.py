class Methods:
    def __init__(self,vertices):
        self.parent = {v: v for v in vertices}
    
    def find(self,item):
        if self.parent[item] == item:
            return item
        return self.find(self.parent[item])
    
    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            return True
        return False
    
def kruskal_algorithm():
    num_vertices = int(input("Ввведите количество деревень"))
    num_edges = int(input("Введите количество возможных дорог"))
    vertices = list(range(1,num_vertices+1))
    edges = []
    print("\nВводите данные о дорогах (Деревня_А Деревня_Б Стоимость):")
    for i in range(num_edges):
        u,v,ves = map(int,input(f"Дорога {i+1}:").split())
        edges.append((ves,u,v))
    edges.sort()
    methods = Methods(vertices)
    answer = []
    total = 0
    for ves,u,v in edges:
        if methods.union(u,v):
            answer.append((u,v,ves))
            total += ves
            if len(answer) == num_vertices -1:
                break
    if len(answer) < num_vertices - 1:
        print("Ошибка: Невозможно соединить все деревни.")
    else:
        print("Построенные дороги:")
        for u, v, ves in answer:
            print(f"{u} - {v} : {ves}")
        print(f"Общая стоимость: {total}")

if __name__ == "__main__":
    kruskal_algorithm()