from collections import deque

graph: dict = {}
graph["you"] = [
    {"name": "Alice", "mango_seller": False},
    {"name": "Bob", "mango_seller": False},
]
graph["Alice"] = [
    {"name": "Peggy", "mango_seller": False},
    {"name": "Anuj", "mango_seller": False},
]
graph["Bob"] = [
    {"name": "Clarie", "mango_seller": False},
    {"name": "John", "mango_seller": True},
    {"name": "Thom", "mango_seller": False},
]
graph["Clarie"] = []
graph["John"] = []
graph["Thom"] = []
graph["Peggy"] = []
graph["Anuj"] = []


def person_is_seller(person: dict) -> bool:
    return person["mango_seller"]


def search(name: str) -> bool:
    search_queue: deque = deque()
    search_queue += graph[name]
    searched: list = []

    while search_queue:
        person: dict = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                return person["name"]
            else:
                search_queue += graph[person["name"]]
                searched.append(person["name"])
    return False


if __name__ == "__main__":
    mango_seller: bool | str = search("you")
    if mango_seller:
        print(f"{mango_seller} is mango seller!")
    else:
        print("You have not found a mango seller")
