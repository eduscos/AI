# Q.2) Implement a system that performs arrangement of some set of objects in a
# room. Assume that you have only 5 rectangular, 4 square-shaped objects. Use A
# approach for the placement of the objects in room for efficient space utilisation.
# Assume suitable heuristic, and dimensions of objects and rooms. (Informed
# Search)
# Ans:-

import heapq
class State:
    def __init__(self, room_width, room_height, remaining_objects, current_state=None):
    self.room_width = room_width
    self.room_height = room_height
    self.remaining_objects = remaining_objects
    if current_state:
        self.placed_objects = current_state.placed_objects.copy()
        self.total_wasted_space = current_state.total_wasted_space
    else:
        self.placed_objects = []
        self.total_wasted_space = 0

def is_goal(self):
    return not self.remaining_objects

def heuristic(self):
    # Simple heuristic: Minimize wasted space
    return self.total_wasted_space

def __lt__(self, other):
    return (self.total_wasted_space + self.heuristic()) < (other.total_wasted_space + other.heuristic())

def a_star(room_width, room_height, object_dimensions):
    initial_state = State(room_width, room_height, object_dimensions)
    priority_queue = [initial_state]
    while priority_queue:
        current_state = heapq.heappop(priority_queue)
        if current_state.is_goal():
            return current_state
        for obj_width, obj_height in current_state.remaining_objects:
            new_state = State(room_width, room_height, current_state.remaining_objects,
            current_state)
            if room_width - obj_width >= 0 and room_height - obj_height >= 0:
                new_state.placed_objects.append((obj_width, obj_height))
                new_state.remaining_objects.remove((obj_width, obj_height))
                new_state.total_wasted_space += room_width * room_height - obj_width *
                obj_height
                heapq.heappush(priority_queue, new_state)
                return None
if __name__ == "__main__":
    room_width = 10
    room_height = 8
    object_dimensions = [(3, 2), (2, 2), (4, 3), (1, 1), (2, 1)]
    result_state = a_star(room_width, room_height, object_dimensions)
    if result_state:
        print("Optimal arrangement:")
        print(result_state.placed_objects)
        print("Total wasted space:", result_state.total_wasted_space)
    else:
        print("No solution found.")
        