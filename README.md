# Predator-Prey Simulation
This project simulates an interactive environment where predators and prey coexist within a 2D grid. The simulation is designed with multiple classes representing various aspects of the environment, agents (predators and prey), and their behaviors.

## Project Structure
```
.
├── main.py         # Entry point of the simulation
├── game.py         # Core game logic and environment management
├── teams.py        # Manages collections of agents (teams)
├── races.py        # Defines behaviors for prey and predators
└── being.py        # Base class for all beings (prey and predators)
```
### Files Overview

- **main.py**
  - **Purpose:** Serves as the main entry point of the simulation.
  - **Details:** Initializes the game, creates teams, and starts the simulation loop.

- **game.py**
  - **Purpose:** Manages the environment and the overall simulation.
  - **Details:** Contains the `Game` and `Map` classes. The `Game` class handles map initialization, team creation, and the simulation's animation.

- **teams.py**
  - **Purpose:** Manages groups of agents, whether predators or prey.
  - **Details:** Defines the `Team` class, responsible for updating member states and managing the addition of new members.

- **races.py**
  - **Purpose:** Defines the specific behaviors of prey and predator agents.
  - **Details:** Contains the `Prey` and `Predator` classes, which manage reproduction, vision, movement, and other behaviors.

- **being.py**
  - **Purpose:** Serves as the base class for all beings within the simulation.
  - **Details:** Defines the `Being` class, which includes fundamental attributes like location, energy, and movement capabilities.

## Dependency Graph
The following graph illustrates the dependencies between the various files:
```
main.py
│
├── game.py
│   ├── teams.py
│   │   └── races.py
│   │       └── being.py
│   └── being.py
└── keyboard (external library)
```
## How to Run
Ensure that all dependencies are installed:
```
pip install numpy matplotlib keyboard
```
To run the simulation:
```
python main.py
```
## Future Enhancements

- **Reinforcement Learning:** Implement a reinforcement learning model for both prey and predators, allowing them to evolve strategies over time.
- **Complex Terrain:** Introduce obstacles or varied terrain to affect movement and visibility, adding more realism to the simulation.
- **Multi-Team Support:** Expand the simulation to support more than two teams, increasing the complexity and dynamics of interactions.
