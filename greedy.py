def find_stantions() -> set:
    states_needed: set = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
    stations: dict = {
        "kone": set(["id", "nv", "ut"]),
        "ktwo": set(["wa", "id", "mt"]),
        "kthree": set(["or", "nv", "ca"]),
        "kfour": set(["nv", "ut"]),
        "kfive": set(["ca", "az"]),
    }
    final_stations: set = set()

    while states_needed:
        best_station: None | str = None
        states_covered: set = set()

        for station, states_for_station in stations.items():
            covered: set = states_needed & states_for_station
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        states_needed -= states_covered
        final_stations.add(best_station)

    return final_stations


if __name__ == "__main__":
    found_stations: set = find_stantions()
    print(
        f"You need to choose next stations: {', '.join(found_stations)}"
    )  # 1, 2, 3, 5
