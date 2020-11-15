from queue import PriorityQueue
import sys

graph = None
number_of_vertexes = None
clients = None

vertex_distance = None
parent_vertexes = None
min_distance_to_server = sys.maxsize


def find_min_distance(N, C, G):
    global graph
    global number_of_vertexes
    global clients
    global min_distance_to_server
    number_of_vertexes = N
    graph = G
    clients = C

    for start_vertex in range(1, number_of_vertexes + 1):
        if start_vertex not in clients:
            candidate = dejkstra(graph, start_vertex)
            if candidate < min_distance_to_server:
                min_distance_to_server = dejkstra(graph, start_vertex)
    return min_distance_to_server

def dejkstra(graph: list, start_vertex: int):
    init_graph_vars(graph, start_vertex)

    available_vertexes_queue = PriorityQueue()
    available_vertexes_queue.put((0, start_vertex))  # [(0,4)]

    while not available_vertexes_queue.empty():
        vertex_to_check = available_vertexes_queue.get()[1]  # 4 #5 #3
        for child_vertex_tuple in graph[vertex_to_check]:  # [(3, 80), (2, 100), (5, 50)] #[(4, 50), (6, 20)] #[(1, 10), (2, 40), (4, 80)]
            child_vertex = child_vertex_tuple[0]  # 3~ 2~ 5~ 4~ 6~ 1~ 2
            distance_to_child_vertex = vertex_distance[vertex_to_check] + child_vertex_tuple[1]  # 80~ 100~ 50~ 80~ 90
            if relax_edge(child_vertex, vertex_to_check, distance_to_child_vertex):
                available_vertexes_queue.put((distance_to_child_vertex, child_vertex))  # [(50, 5), ~(80, 3)~, (80,5), (100,2), (90,3)]:
    return get_max_distance_to_clients();


def relax_edge(child_vertex, parent_vertex, distance):
    if vertex_distance[child_vertex] > distance:
        parent_vertexes[child_vertex] = parent_vertex  # [ , 3, 4, 4, , 4, 5]
        vertex_distance[child_vertex] = distance  # [ , 90, 100, 80, ,50, 80]
        return True
    return False


def init_graph_vars(graph: list, start_vertex: int):
    global vertex_distance
    global parent_vertexes
    vertex_distance = []
    parent_vertexes = []
    for vertex in graph:
        vertex_distance.append(sys.maxsize)
        parent_vertexes.append(None)
    vertex_distance[start_vertex] = 0


def get_max_distance_to_clients():
    distances_to_clients = []
    for client_vertex in clients:
        distances_to_clients.append(vertex_distance[client_vertex])
    return max(distances_to_clients)
