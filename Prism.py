# Vertices of a triangular prism
verticies = (
    (1, 0, -1),  # Front base right vertex
    (0, 1, -1),  # Front base top vertex
    (-1, 0, -1), # Front base left vertex
    (1, 0, 1),   # Back base right vertex
    (0, 1, 1),   # Back base top vertex
    (-1, 0, 1)   # Back base left vertex
)

# Edges for the triangular prism
edges = (
    (0, 1), # Front base right to top
    (1, 2), # Front base top to left
    (2, 0), # Front base left to right
    (3, 4), # Back base right to top
    (4, 5), # Back base top to left
    (5, 3), # Back base left to right
    (0, 3), # Sides right vertices
    (1, 4), # Sides top vertices
    (2, 5)  # Sides left vertices
)

# Corrected surfaces for the triangular prism
surfaces = (
    (0, 1, 2, 4), # Front base
    (3, 4, 5, 2), # Back base
    (0, 1, 4, 3), # Side 1
    (1, 2, 5, 4), # Side 2
    (2, 0, 3, 5)  # Side 3
)

# Colors for the triangular prism surfaces
colors = (
    (1, 0, 0), # Red for the front base
    (0, 1, 0), # Green for the back base
    (0, 0, 1), # Blue for side 1
    (1, 1, 0), # Yellow for side 2
    (1, 0, 1)  # Magenta for side 3
)

