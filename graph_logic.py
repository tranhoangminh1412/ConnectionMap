from collections import deque

# Function to find the nearest connection in the user's network that leads to the target
def find_nearest_connection(graph, start, target):
    if start not in graph or target not in graph:
        return None

    # Queue stores tuples of (current user, path to current user)
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current_user, path = queue.popleft()
        
        # Check if we reached the target
        if current_user == target:
            # The second element in the path is the nearest connection from the start
            if len(path) > 1:
                return path[1], len(path) - 1  # Nearest connection, level of connection
            else:
                return start, 0  # Direct connection case

        visited.add(current_user)

        # Explore neighbors
        for neighbor in graph.neighbors(current_user):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None  # No connection found
