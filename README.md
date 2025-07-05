# Graph Labeling Optimizer

A Python-based toolkit for solving and visualizing node labeling problems on tree-structured graphs. Each graph is given as an adjacency list, and the goal is to assign labels (colors) to nodes subject to problem-specific constraints.

This project includes:
- A labeling algorithm (custom solver)
- Test data handling for small, medium, and large graph instances
- Graph visualizations with label-aware coloring
- Support for batch testing and saving solutions

---

## Documentation

For full details of the problem and algorithm, refer to the PDFs below:

- [Problem Description (PDF)](docs/problem.pdf)  
  Defines the node labeling problem, input format, constraints, and examples.

- [Algorithm Description (PDF)](docs/algorithm.pdf)  
  Explains the algorithmic approach, proof of optimality, and solver implementation.


## Project Structure

```bash
graph-labeling-optimizer/
├── solver.py # Your custom labeling algorithm
├── main.py # Runs the algorithm on test data and plots graph labeling
├── data/
│ ├── instances/ # Graph adjacency lists and label counts
│ └── solutions/ # Precomputed solutions (pickled)
├── docs/
│   ├── problem.pdf
│   └── algorithm.pdf
├── viz_labels/ # Visualization of graph labeling
├── requirements.txt
├── README.md
```

## Problem Overview

Given:
- A **tree graph** (as an adjacency list)
- A **label count** `k` for each graph

Goal:
- Assign a label (from `0` to `k-1`) to each node
- Satisfy constraints defined in the labeling problem (e.g., proximity rules)


## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/axgeorge/graph-labeling-optimizer.git
cd graph-labeling-optimizer
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### Running Tests and Visualizing

To run the algorithm on a specific test set:

Inside `main.py`, choose your test set:

```python
# Choose which test to run. Saving solution is required for visualization.
# Comment out block if not running tests.

test_key = "small"  # Options: small, medium, large, set_small, set_medium, set_large, example
tree_file, label_file = TEST_FILES[test_key]
check_validity = False
save = False
main(test_key, tree_file, label_file, check_validity, save)
```

To visualize an instance:

Inside `main.py`, choose your test set and instance index:

```python
# Plot an instance solution.
test_key = "set_small" # Options: small, medium, large, set_small, set_medium, set_large, example
index = 0
plot_instance_solution(test_key, index)
```

Finally, run the file

```bash
python main.py
```

