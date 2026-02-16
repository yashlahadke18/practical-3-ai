import streamlit as st
from collections import deque

st.title("Water Jug Problem using BFS")

st.write("Solve the Water Jug Problem using Breadth First Search.")

# BFS Function
def water_jug_bfs(capA, capB, target):
    visited = set()
    queue = deque()
    parent = {}

    queue.append((0, 0))
    visited.add((0, 0))

    while queue:
        a, b = queue.popleft()

        # Check if target reached
        if a == target or b == target:
            path = []
            while (a, b) != (0, 0):
                path.append((a, b))
                a, b = parent[(a, b)]
            path.append((0, 0))
            return path[::-1]

        # Possible moves
        moves = [
            (capA, b),  # Fill Jug A
            (a, capB),  # Fill Jug B
            (0, b),     # Empty Jug A
            (a, 0),     # Empty Jug B
            (min(capA, a+b), max(0, a+b - capA)),  # Pour B → A
            (max(0, a+b - capB), min(capB, a+b))   # Pour A → B
        ]

        for move in moves:
            if move not in visited:
                visited.add(move)
                parent[move] = (a, b)
                queue.append(move)

    return None


# User Inputs
capA = st.number_input("Capacity of Jug A:", min_value=1, value=4)
capB = st.number_input("Capacity of Jug B:", min_value=1, value=3)
target = st.number_input("Target Amount:", min_value=1, value=2)

# Run Button
if st.button("Find Solution"):
    solution = water_jug_bfs(capA, capB, target)

    if solution:
        st.success("Solution Steps:")
        for step in solution:
            st.write(step)
    else:
        st.error("No solution found.")
