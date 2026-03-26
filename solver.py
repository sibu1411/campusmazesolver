import collections
campusmap = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0]
]
start=(0,0)
goal=(6,6)

def bfs(grid, start, goal):
  queue = collections.deque([start])
    visited = {start}
    parent = {start: None}  
    nodes_explored = 0
while queue:
        current = queue.popleft()
        nodes_explored += 1
  if current == goal:
            return reconstruct_path(parent, goal), nodes_explored
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = (current[0] + dx, current[1] + dy)
      if (0 <= neighbor[0] < len(grid) and 
                0 <= neighbor[1] < len(grid[0]) and 
                grid[neighbor[0]][neighbor[1]] == 0 and 
                neighbor not in visited):
                
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    
    return None, nodes_explore
