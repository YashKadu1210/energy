def bfs(start, goal):
    parent = []
    queue = []
    explored = []
    queue.append(start)

    while queue:
        # Fill jug A from the tap
        child1 = fill_A_from_tap(queue[0])
        if child1 != None:
            if child1 not in explored and child1 not in queue:
                queue.append(child1)
                parent.append([queue[0], child1])
            if child1 == goal:
                print("Found")
                print(find_path(parent))
                return

        # Fill jug B from the tap
        child1 = fill_B_from_tap(queue[0])
        if child1 != None:
            if child1 not in explored and child1 not in queue:
                queue.append(child1)
                parent.append([queue[0], child1])
            if child1 == goal:
                print("Found")
                print(find_path(parent))
                return

        # Pour water from jug A to jug B
        child1 = from_A_to_B(queue[0])
        if child1 != None:
            if child1 not in explored and child1 not in queue:
                queue.append(child1)
                parent.append([queue[0], child1])
            if child1 == goal:
                print("Found")
                print(find_path(parent))
                return

        # Pour water from jug B to jug A
        child1 = from_B_to_A(queue[0])
        if child1 != None:
            if child1 not in explored and child1 not in queue:
                queue.append(child1)
                parent.append([queue[0], child1])
            if child1 == goal:
                print("Found")
                print(find_path(parent))
                return

        explored.append(queue[0])
        print(explored)
        queue.pop(0)


def find_path(parents):
    path = []
    path.append(parents[len(parents)-1][1])

    for i in range(len(parents)-2, -1, -1):
        if parents[i][1] == path[-1]:
            path.append(parents[i][0])
    path.reverse()
    return path

# Helper functions to simulate jug operations


A_capacity = 4
B_capacity = 3


def fill_A_from_tap(state):
    # Fill jug A to its full capacity
    return (A_capacity, state[1])


def fill_B_from_tap(state):
    # Fill jug B to its full capacity
    return (state[0], B_capacity)


def from_A_to_B(state):
    # Pour water from jug A to jug B
    A, B = state
    pour = min(A, B_capacity - B)
    return (A - pour, B + pour)


def from_B_to_A(state):
    # Pour water from jug B to jug A
    A, B = state
    pour = min(B, A_capacity - A)
    return (A + pour, B - pour)


# Example usage:
start_state = (0, 0)
goal_state = (0, 2)
bfs(start_state, goal_state)