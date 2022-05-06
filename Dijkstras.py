INFINITY: float = float("inf")
graph: dict = {}
processed: list = []

graph["start"] = {"a": 6, "b": 2}
graph["a"] = {"fin": 1}
graph["b"] = {"a": 3, "fin": 5}
graph["fin"] = {}

costs: dict = {"a": 6, "b": 2, "fin": INFINITY}

parents: dict = {"a": "start", "b": "start", "fin": None}


def find_lowest_cost_node(costs: dict) -> None | str:
    lowest_cost: float = INFINITY
    lowest_cost_node: None | str = None

    for node in costs:
        cost: int | float = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


def find_nodes() -> None:
    node: None | str = find_lowest_cost_node(costs)
    while node is not None:
        cost: int | float = costs[node]
        neighbors: dict = graph[node]
        for k in neighbors.keys():
            new_cost: int | float = cost + neighbors[k]
            if costs[k] > new_cost:
                costs[k] = new_cost
                parents[k] = node
        processed.append(node)
        node: None | str = find_lowest_cost_node(costs)


if __name__ == "__main__":
    find_nodes()
    print(f"Lowest cost way: start -> {' -> '.join(processed)}")
