```python
import heapq
import logging

class Labirinto:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def astar(self):
        frontier = []
        heapq.heappush(frontier, (0, self.start))
        came_from = {}
        cost_so_far = {}
        came_from[self.start] = None
        cost_so_far[self.start] = 0

        while frontier:
            current = heapq.heappop(frontier)[1]

            if current == self.goal:
                break

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_cell = (current[0] + dx, current[1] + dy)
                if (0 <= next_cell[0] < len(self.grid) and
                    0 <= next_cell[1] < len(self.grid[0]) and
                    self.grid[next_cell[0]][next_cell[1]] == 0):
                    new_cost = cost_so_far[current] + 1
                    if next_cell not in cost_so_far or new_cost < cost_so_far[next_cell]:
                        cost_so_far[next_cell] = new_cost
                        priority = new_cost + self.heuristic(self.goal, next_cell)
                        heapq.heappush(frontier, (priority, next_cell))
                        came_from[next_cell] = current

        if current != self.goal:
            return "Nessun percorso possibile"

        path = []
        step = current
        while step:
            path.append(step)
            step = came_from.get(step)
        path.reverse()

        return path

    def __str__(self):
        return str(self.grid)

def main():
    grid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    start = (0, 0)
    goal = (2, 2)
    labirinto = Labirinto(grid, start, goal)
    logging.info("Inizia ricerca percorso...")
    path = labirinto.astar()
    logging.info("Percorso trovato: %s", path)

if __name__ == "__main__":
    main()
```
This code defines a `Labirinto` class that implements the A* algorithm to find the shortest path from a start to a goal position in a grid. The `main` function creates a grid, sets the start and goal positions, and runs the A* algorithm to find the path. The code includes logging statements to track the progress of the algorithm.