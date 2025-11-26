import os
import sys
import pytest

# Ensure we can import main.py from the homework folder
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import shortest_path


@pytest.mark.parametrize(
    "rooms, doors, start, goal, expected",
    [
        ([], [], "A", "A", []),
        (["A"], [], "A", "A", ["A"]),
        (["A", "B"], [("A", "B")], "A", "B", ["A", "B"]),
        (["A", "B"], [], "A", "B", []),
    ],
)
def test_basic_cases(rooms, doors, start, goal, expected):
    assert shortest_path(rooms, doors, start, goal) == expected


@pytest.mark.parametrize(
    "rooms, doors, start, goal, expected",
    [
        (
            ["Entrance", "Hall", "Gallery", "Cafe"],
            [("Entrance", "Hall"), ("Hall", "Gallery"), ("Gallery", "Cafe")],
            "Entrance",
            "Cafe",
            ["Entrance", "Hall", "Gallery", "Cafe"],
        ),
        (
            ["R1", "R2", "R3", "R4"],
            [("R1", "R2"), ("R2", "R3"), ("R1", "R3")],
            "R1",
            "R3",
            # Unique shortest path is length 2: R1->R3
            ["R1", "R3"],
        ),
        (
            ["A", "B", "C", "D", "E"],
            [("A", "B"), ("B", "C"), ("C", "D"), ("B", "D")],
            "A",
            "D",
            # Shortest path is A-B-D (length 3)
            ["A", "B", "D"],
        ),
    ],
)
def test_simple_paths(rooms, doors, start, goal, expected):
    assert shortest_path(rooms, doors, start, goal) == expected


@pytest.mark.parametrize(
    "rooms, doors, start, goal, expected_len",
    [
        (
            ["R" + str(i) for i in range(6)],
            [("R0", "R1"), ("R1", "R2"), ("R2", "R3"), ("R3", "R4"), ("R4", "R5")],
            "R0",
            "R5",
            6,
        ),
        (
            ["A", "B", "C", "D", "E", "F"],
            [
                ("A", "B"),
                ("B", "C"),
                ("C", "D"),
                ("D", "E"),
                ("C", "F"),
            ],
            "A",
            "F",
            4,  # A-B-C-F
        ),
        (
            ["X1", "X2", "X3", "X4", "X5"],
            [
                ("X1", "X2"),
                ("X2", "X3"),
                ("X3", "X4"),
                ("X4", "X5"),
                ("X1", "X3"),
                ("X2", "X4"),
            ],
            "X1",
            "X5",
            4,  # one shortest path length
        ),
    ],
)
def test_larger_graphs_and_lengths(rooms, doors, start, goal, expected_len):
    path = shortest_path(rooms, doors, start, goal)
    assert path[0] == start
    assert path[-1] == goal
    assert len(path) == expected_len

    # Check that every step uses a real door
    door_set = {tuple(sorted(d)) for d in doors}
    for a, b in zip(path, path[1:]):
        assert tuple(sorted((a, b))) in door_set
