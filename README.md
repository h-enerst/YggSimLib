# YggSimLib

YggSimLib is a Python framework for orchestrating and automating simulation workflows in the Yggdrasil Engineering Simulator. It allows for modular control of simulated equipment such as valves, motors, heaters, PID controllers, and choke valves, and supports stepwise and parallel sequence execution with inhibit logic and transition conditions.

## 🔧 Features

- Object-oriented wrappers for:
  - On/off valves
  - Electric motors and heaters
  - PID controllers
  - Choke valves
  - Transmitters
- Flexible step-based sequencer (`Step`, `Sequence`)
- Inhibit logic for conditional execution
- Dependency-managed sequence orchestration via `Admin`
- GUI support for selecting models, timelines, and data files
- Parallel execution support using threads

## 📁 File Structure

- `YggSimLib.py`: Core library with class definitions and sequence execution engine
- `muninUtilities.py`: Example configuration for a multi-system simulation setup
- `main.py`: Startup script to initialize and run the sequences

## 🚀 Quick Start

```bash
python main.py
```

### GUI Prompts
You’ll be prompted to select:
1. Simulation model directory
2. Timeline
3. Model, parameter, and initial condition files

Once loaded, the simulation sequences will begin executing according to defined dependencies.

## 🧠 Example: Defining a Step

```python
step = Step({
    "number": 10,
    "actions": [valve.open],
    "transitions": [valve.is_open],
    "tmax": 30,
    "next": lambda: "S020"
})
```

## 🔁 Sequence Logic

```python
steps = {"S010": step1, "S020": step2}
sequence = Sequence("pump_start", steps, sim)
sequence.add_steps(steps.values())
sequence.start()
```

## 🧩 Admin Graph
Use `Admin` to define a full system of sequences with dependencies:

```python
a = Admin("startup_controller", [seq1, seq2, seq3], edges, sim)
a.start()
```

## 📚 Documentation Style
Docstrings follow the Google Python style guide and describe:
- Arguments
- Behavior
- Return values (where applicable)

## ✅ Requirements
- Python 3.12
- Yggdrasil Engineering Simulator (with `kspice` Python bindings)
- `networkx` for dependency graphs

## ✨ Author
Built by Håkon – Process Data Scientist, passionate about simulation, optimization.
