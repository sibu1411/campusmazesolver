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
Manhattan Distance Formula:d=x1 - x2 + y1 - y2
Conclusion & KeyTakeaways:
This project successfully demonstrates that *Informed Search (A)** is significantly more efficient than Uninformed Search (BFS) for navigation tasks. By using a Manhattan Distance heuristic, the agent was able to ignore 60% of the 'wrong' directions that BFS explored, proving that a little bit of knowledge goes a long way in AI.

<img width="1690" height="938" alt="Screenshot 2026-03-28 160128" src="https://github.com/user-attachments/assets/3f9f08d4-f312-404e-be51-e7b3e7f19d38" />
<img width="1301" height="938" alt="Screenshot 2026-03-28 160150" src="https://github.com/user-attachments/assets/762aed6a-8efe-46e2-8858-fe9f996d5888" />
<img width="1113" height="881" alt="Screenshot 2026-03-28 160207" src="https://github.com/user-attachments/assets/1f22aed2-383f-4e7b-8ce6-0761fc0dc12f" />
<img width="489" height="314" alt="Screenshot 2026-03-28 160251" src="https://github.com/user-attachments/assets/1978c145-0f1a-4925-9758-42decd3d0a5f" />



