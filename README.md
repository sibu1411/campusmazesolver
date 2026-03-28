#  Campus Navigation: The "Maze Solver" Agent

**A 1st-Year AI & ML Student Project | Module 2: Search Strategies**

###  The Problem

Imagine you are at the **Hostel (S)** and need to get to the **AI Lab (G)** for a morning class. The campus isn't just an empty field—there are buildings, walls, and restricted zones (**\#**) in your path.

I built this Python-based "Problem-Solving Agent" to figure out the best way to navigate a 7x7 grid using two different types of "AI brains": **BFS** (Uninformed) and **A**\* (Informed).

###  How the Agent "Thinks"

| Algorithm | The Strategy | My Observation |
| :--- | :--- | :--- |
| **BFS** | "The Blind Wanderer" | It checks every single direction equally. It's guaranteed to find the shortest path, but it wastes a lot of energy looking at walls. |
| **A* Search*\* | "The Smart Navigator" | It uses a **Heuristic (Manhattan Distance)** to "sense" where the Goal is. It's much more efficient because it focuses on moving toward the target. |


###  Real-World Results

When I ran the code on my campus map, here is how the agent performed:

  * **Path Found:** Yes (19 steps total).
  * **Efficiency Win:** While BFS had to "look" at **24** different coordinates, A\* found the same path by only checking **\~21** spots.
  * **The Math:** A\* uses the evaluation function **f(n) = g(n) + h(n)** to stay on track.

### 🛠️ Project Structure

  * `src/solver.py`: The core logic for the BFS and A\* algorithms.
  * `requirements.txt`: Standard Python environment setup (no external libraries required).
  * `.gitignore`: Keeps the repository clean by hiding temporary `__pycache__` files.
  * `LICENSE`: MIT License (open for others to learn from\!).


###  How to Run the Solver

To test the agent on your own machine, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/Campus-Maze-Solver.git
    cd Campus-Maze-Solver
    ```
2.  **Run the Script:**
    Execute the main solver file from your terminal:
    ```bash
    python src/solver.py
    ```
3.  **Interpret the Map:**
      * **S** = Hostel (Start)
      * **G** = AI Lab (Goal)
      * **\#** = Buildings (Obstacles)
      * **\*** = The path discovered by the AI\!


###  What I Learned

This project was a deep dive into **State Space Search**. I realized that "Intelligence" in AI often just means giving an algorithm a little bit of "context" (like a Heuristic) so it doesn't have to guess. It taught me how to turn a physical location into a discrete grid that a computer can solve.


**Created by:** Smruti Sagar Sethy(25BAI11138)  
**Major:** B.Tech in Artificial Intelligence & Machine Learning


<img width="1690" height="938" alt="Screenshot 2026-03-28 160128" src="https://github.com/user-attachments/assets/dc174cdf-dc5d-4101-8f81-f253f187a2c6" />

<img width="1301" height="938" alt="Screenshot 2026-03-28 160150" src="https://github.com/user-attachments/assets/7ace5aaa-a017-4f80-9c4f-39e90bc853de" />

<img width="1113" height="881" alt="Screenshot 2026-03-28 160207" src="https://github.com/user-attachments/assets/0ac0d3d3-799c-4d88-9165-b99fd378e729" />

<img width="489" height="314" alt="Screenshot 2026-03-28 160251" src="https://github.com/user-attachments/assets/c606b13b-87d1-4597-b911-1fb51b15a966" />



