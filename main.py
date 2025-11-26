


def shortest_path(rooms, doors, start, goal):
    """
    Compute one shortest path between start and goal in an undirected graph.

    rooms: list of room name strings.
    doors: list of (a, b) pairs, each pair is an undirected door between rooms a and b.
    start: start room name.
    goal: goal room name.

    Return:
      - list of room names from start to goal (inclusive) for one shortest path,
      - [start] if start == goal,
      - [] if no path exists.
    """

    # TODO Steps 1–3: Restate the problem and choose a graph representation.
    # TODO Steps 4–5: Plan a BFS that tracks parents and stops when goal is found.
    # TODO Step 6: Implement BFS and path reconstruction.
    # TODO Step 7: Test with small maps (lines, branches, isolated rooms).
    # TODO Step 8: Confirm complexity is about O(n + m).
    pass


if __name__ == "__main__":
    # Optional manual test
    rooms = ["Entrance", "Hall", "Gallery", "Cafe"]
    doors = [("Entrance", "Hall"), ("Hall", "Gallery"), ("Gallery", "Cafe")]
    print(shortest_path(rooms, doors, "Entrance", "Cafe"))
