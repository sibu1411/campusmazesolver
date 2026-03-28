# campusmazesolver
A Pythonbased pathfinding agent that navigates a simulated campus grid using BFS(Uninformed) and A*(Informed) search strategies.
Campus Navigation Maze SolverCourse Connection: Module 2 - Search Strategies (Uninformed vs. Informed)
Overview:This project implements a Problem-Solving Agent designed to find the most efficient path between two points on a university campus (e.g., from a Hostel to a Lab).The goal is to navigate a 2D grid while avoiding "dead zones" or obstacles (buildings). This project specifically compares how a "blind" search compares to a "smart" search using heuristics.
FeaturesEnvironment:A 2D Matrix representing the campus grid.0: Walkable path.1: Obstacle/Building.
Algorithms:BFS(Breadth-First Search): An uninformed search that explores all possibilities layer-by-layer.A (A-Star)
Search: An informed search that uses a heuristic to target the goal.
Heuristic Function: Uses Manhattan Distance to calculate the estimated cost to the destination.
Technical Logic:The core of the Informed Search (A*) is the evaluation function:f(n) = g(n) + h(n) 
g(n):The actual cost from the start node to the current node n.
h(n):The estimated cost from n to the goal (Manhattan Distance).
Manhattan Distance Formula:d=|x1 - x2| + |y1 - y2|
Conclusion & KeyTakeaways:
This project successfully demonstrates that *Informed Search (A)** is significantly more efficient than Uninformed Search (BFS) for navigation tasks. By using a Manhattan Distance heuristic, the agent was able to ignore 60% of the 'wrong' directions that BFS explored, proving that a little bit of knowledge goes a long way in AI.



<img width="1690" height="938" alt="Screenshot 2026-03-28 160128" src="https://github.com/user-attachments/assets/dc174cdf-dc5d-4101-8f81-f253f187a2c6" />

<img width="1301" height="938" alt="Screenshot 2026-03-28 160150" src="https://github.com/user-attachments/assets/7ace5aaa-a017-4f80-9c4f-39e90bc853de" />

<img width="1113" height="881" alt="Screenshot 2026-03-28 160207" src="https://github.com/user-attachments/assets/0ac0d3d3-799c-4d88-9165-b99fd378e729" />

<img width="489" height="314" alt="Screenshot 2026-03-28 160251" src="https://github.com/user-attachments/assets/c606b13b-87d1-4597-b911-1fb51b15a966" />



