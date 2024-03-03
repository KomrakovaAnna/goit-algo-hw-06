import networkx as nx
import matplotlib.pyplot as plt


#ЗАВДАННЯ 1
metro_graph = nx.Graph()

stations_metro_red = [
    "Академмістечко", "Житомирська", "Святошин", "Нивки", "Берестейська",
    "Шулявська", "Політехнічний інститут", "Вокзальна", "Університет",
    "Театральна", "Хрещатик", "Арсенальна", "Дніпро", "Гідропарк",
    "Лівобережна","Дарниця", "Чернігівська", "Лісова",
]
stations_metro_green = [
    "Сирець", "Дорогожичі", "Лук'янівська", "Золоті ворота", "Палац Спорту",
    "Кловська", "Печерська", "Звіринецька", "Видубичі",
    "Славутич", "Осокорки", "Позняки", "Харківська", "Вирлиця",
    "Бориспільська", "Червоний Хутір"
]
stations_metro_blue = [
    "Героїв Дніпра", "Мінська", "Оболонь", "Почайна", "Тараса Шевченка",
    "Контрактова Площа", "Поштова Площа", "Майдан Незалежності", "Площа Українських Героїв",
    "Олімпійська", "Палац Україна", "Либідська", "Деміївська", "Голосіївська",
    "Васильківська", "Виставковий центр", "Іподром", "Теремки"
]

metro_graph.add_nodes_from(stations_metro_red)
metro_graph.add_nodes_from(stations_metro_green)
metro_graph.add_nodes_from(stations_metro_blue)

connections = [
    ("Академмістечко", "Житомирська"),
    ("Житомирська", "Святошин"),
    ("Святошин", "Нивки"),
    ("Нивки", "Берестейська"),
    ( "Берестейська", "Шулявська"),
    ("Шулявська", "Політехнічний інститут"),
    ("Політехнічний інститут", "Вокзальна"),
    ("Вокзальна", "Університет"),
    ("Університет", "Театральна"),
    ("Театральна", "Хрещатик"),
    ("Хрещатик", "Арсенальна"),
    ("Арсенальна", "Дніпро"),
    ("Дніпро", "Гідропарк"),
    ("Гідропарк", "Лівобережна"),
    ("Лівобережна","Дарниця"),
    ("Дарниця", "Чернігівська"),
    ("Чернігівська", "Лісова"),
    ("Сирець", "Дорогожичі"),
    ("Дорогожичі", "Лук'янівська"),
    ("Лук'янівська", "Золоті ворота"),
    ("Золоті ворота", "Палац Спорту"),
    ("Палац Спорту", "Кловська"),
    ("Кловська", "Печерська"),
    ("Печерська", "Звіринецька"),
    ("Звіринецька", "Видубичі"),
    ("Видубичі", "Славутич"),
    ("Славутич", "Осокорки"),
    ("Осокорки", "Позняки"),
    ("Позняки", "Харківська"),
    ("Харківська", "Вирлиця"),
    ("Вирлиця", "Бориспільська"),
    ("Бориспільська", "Червоний Хутір"),
    ("Героїв Дніпра", "Мінська"),
    ("Мінська", "Оболонь"),
    ("Оболонь", "Почайна"),
    ("Почайна", "Тараса Шевченка"),
    ("Тараса Шевченка", "Контрактова Площа"),
    ("Контрактова Площа", "Поштова Площа"),
    ("Поштова Площа", "Майдан Незалежності"),
    ("Майдан Незалежності", "Площа Українських Героїв"),
    ("Площа Українських Героїв", "Олімпійська"),
    ("Олімпійська", "Палац Україна"),
    ("Палац Україна", "Либідська"),
    ("Либідська", "Деміївська"),
    ("Деміївська", "Голосіївська"),
    ("Голосіївська", "Васильківська"),
    ("Васильківська", "Виставковий центр"),
    ("Виставковий центр", "Іподром"),
    ("Іподром", "Теремки"),
    ("Золоті ворота", "Театральна"),
    ("Хрещатик", "Майдан Незалежності"),
    ("Площа Українських Героїв", "Палац Спорту")
]

# Додамо з'єднання між станціями до графа
metro_graph.add_edges_from(connections)

# Візуалізуємо граф
plt.figure(figsize=(15, 10))
pos = nx.spring_layout(metro_graph)  # Позиціонування вершин графа
nx.draw(metro_graph, pos, with_labels=True, node_size=10, node_color='lightblue', font_size=10)
plt.title('Метро міста')
plt.show()

# Проведемо аналіз характеристик графа
print("Кількість вершин:", metro_graph.number_of_nodes())
print("Кількість ребер:", metro_graph.number_of_edges())

# Обчислимо середній ступінь вершин
average_degree = sum(dict(metro_graph.degree()).values()) / metro_graph.number_of_nodes()
print("Середній ступінь вершин:", average_degree)

# Знайдемо вершину з максимальним ступенем
max_degree_node, max_degree = max(dict(metro_graph.degree()).items(), key=lambda x: x[1])
print("Вершина з найбільшим ступенем:", max_degree_node, "із ступенем", max_degree)


#ЗАВДАННЯ 2 : BFS&DFS

def dfs_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = dfs_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

def bfs_paths(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (node, path) = queue.pop(0)
        for next_node in set(graph[node]) - set(path):
            if next_node == end:
                yield path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))


start_station = "Університет"
end_station = "Поштова Площа"
dfs_path = next(iter(dfs_paths(metro_graph, start_station, end_station)), None)
print("Шлях за допомогою DFS:", dfs_path)

# Знайдемо шляхи за допомогою BFS
bfs_path = next(bfs_paths(metro_graph, start_station, end_station), None)
print("Шлях за допомогою BFS:", bfs_path)


#ЗАВДАННЯ 3 
def dijkstra(graph, start):
    # Ініціалізуємо словник для зберігання найкоротших відстаней
    # від початкової вершини до всіх інших вершин
    distances = {node: float('inf') for node in graph.nodes()}
    distances[start] = 0  
    visited = set()  

    while len(visited) < len(graph.nodes()):
        
        current_node = min((node for node in graph.nodes() if node not in visited),
                           key=lambda x: distances[x])

        
        visited.add(current_node)

       
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances

#  зваження до ребер графа
for edge in connections:
    weight = 1 
    metro_graph.add_edge(edge[0], edge[1], weight=weight)

# Знаходимо найкоротші шляхи від кожної вершини до всіх інших
all_shortest_paths = {}
for node in metro_graph.nodes():
    all_shortest_paths[node] = dijkstra(metro_graph, node)

#  результати
    
"""
for node in metro_graph.nodes():
    print(f"Найкоротші шляхи з вершини {node}:")
    for target_node, distance in all_shortest_paths[node].items():
        print(f"До вершини {target_node}: відстань {distance}")

"""