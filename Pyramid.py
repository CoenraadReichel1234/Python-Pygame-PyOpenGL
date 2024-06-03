# Vertices of a triangular pyramid (tetrahedron)
verticies = (
    (0, 1, 0),  # Top vertex
    (1, -1, 1), # Base vertex 1
    (-1, -1, 1),# Base vertex 2
    (-1, -1, -1)# Base vertex 3
)

# Edges for the triangular pyramid
edges = (
    (0, 1), # Edge from top vertex to base vertex 1
    (0, 2), # Edge from top vertex to base vertex 2
    (0, 3), # Edge from top vertex to base vertex 3
    (1, 2), # Edge connecting base vertex 1 and base vertex 2
    (2, 3), # Edge connecting base vertex 2 and base vertex 3
    (3, 1)  # Edge connecting base vertex 3 and base vertex 1
)

# Corrected surfaces for the triangular pyramid (tetrahedron)
surfaces = (
    (0, 1, 2), # Base
    (0, 1, 3), # Side 1
    (0, 2, 3), # Side 2
    (1, 2, 3)  # Side 3
)


# Colors for the triangular pyramid surfaces
colors = (
    (1, 0, 0), # Red
    (0, 1, 0), # Green
    (0, 0, 1), # Blue
    (1, 1, 0)  # Yellow
)

