from typing import List


class Graph:
    def __init__(self, rowptr: List[int], colidx: List[int], values: List[float]):
        self._rowptr: List[int] = rowptr
        self._colidx: List[int] = colidx
        self._values: List[float] = values

    def rowptr(self) -> List[int]:
        return self._rowptr

    def colidx(self) -> List[int]:
        return self._colidx

    def values(self) -> List[float]:
        return self._values


def load_graph() -> Graph:
    rowptr = [0, 1, 3, 5, 5, 5]
    colidx = [1, 2, 5, 3, 4, 3]
    values = [1.1, 2.3, 3.7, 0.5, 1.9, 1.8]
    return Graph(rowptr, colidx, values)


def init_distances(graph: Graph, source: int) -> List[float]:
    distances = [1000000.0 for _ in range(len(graph.colidx()))]
    distances[source] = 0.0
    return distances


def sssp(graph: Graph, source: int) -> List[float]:
    distances = init_distances(graph, source)

    while True:
        is_updated = False

        for vertex in range(len(graph.colidx())):
            neighbor_begin = graph.rowptr()[vertex]

            if vertex == len(graph.colidx()) - 1:
                neighbor_end = len(graph.colidx()) - 1
            else:
                neighbor_end = graph.rowptr()[vertex + 1]

            for neighbor in range(neighbor_begin, neighbor_end):
                neighbor_vertex = graph.colidx()[neighbor]

                new_distance = distances[vertex] + graph.values()[neighbor]
                cur_distance = distances[neighbor_vertex]

                if new_distance < cur_distance:
                    distances[neighbor_vertex] = new_distance
                    is_updated = True

        if not is_updated:
            break
    return distances


if __name__ == "__main__":
    graph = load_graph()
    source = 0
    distances = sssp(graph, source)
    print(f"distances: {distances}")
