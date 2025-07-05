    
import pickle
import solver
from pathlib import Path

# ====== Configuration ======

TEST_PATH = Path("data/instances")  
SOL_PATH = Path("data/solutions")

TEST_FILES = {
    "small": ("Small_Examples_of_AdjLists_of_Trees", "Small_Examples_of_k_values"),
    "medium": ("Medium_Examples_of_AdjLists_of_Trees", "Medium_Examples_of_k_values"),
    "large": ("Large_Examples_of_AdjLists_of_Trees", "Large_Examples_of_k_values"),
    "set_small": ("Test_Set_Small_AdjLists_of_Trees", "Test_Set_Small_of_k_values"),
    "set_medium": ("Test_Set_Medium_AdjLists_of_Trees", "Test_Set_Medium_of_k_values"),
    "set_large": ("Test_Set_Large_AdjLists_of_Trees", "Test_Set_Large_of_k_values"),
    "example": ("Examples_of_AdjLists_of_Trees", "Examples_of_k_values")
}

SOLUTION_FILES = {
    "small": "small_solutions",
    "medium": "medium_solutions",
    "large": "large_solutions",
    "set_small": "set_small_solutions",
    "set_medium": "set_medium_solutions",
    "set_large": "set_large_solutions",
    "example": "example_solutions",
    "example_reference": "Examples_of_labelling"
}


# ====== Utility Functions ======

def load_pickle(path):
    with open(path, "rb") as f:
        return pickle.load(f)

def save_pickle(data, path):
    with open(path, "wb") as f:
        pickle.dump(data, f)

def run_labeling_tests(tree_list, label_list, root=0, check=False):
    sol_list = []
    for i, (tree, k) in enumerate(zip(tree_list, label_list)):
        print(f"Started test {i}")
        labeling = solver.labeling_algorithm(tree, root, k)
        sol_list.append(labeling)
        # Optionally validate:
        if check:
            sol = solver.find_proximity(tree, root, k, labeling)
            if sol != 1:
                print(f"WARNING: PROXIMITY RATIO ERROR. A RATIO {sol} DETECTED")
            solver.check_validity(tree, k, labeling)
    return sol_list

def main(test_key, tree_file, label_file, check_validity, save):
    # Load test data
    tree_path = TEST_PATH / tree_file
    label_path = TEST_PATH / label_file
    
    if not tree_path.exists() or not label_path.exists():
        raise FileNotFoundError(f"Missing input file(s): {tree_path}, {label_path}")
    
    trees = load_pickle(tree_path)
    labels = load_pickle(label_path)

    # Run labeling algorithm
    solutions = run_labeling_tests(trees, labels, check=check_validity)

    # Save the solution (optional)
    if save:
        if test_key in SOLUTION_FILES:
            solution_file = SOLUTION_FILES[test_key]
            save_path = SOL_PATH / solution_file
            save_pickle(solutions, save_path)
            print(f"Completed {len(trees)} test cases for '{test_key}'.")
            print(f"Solutions saved to {save_path}")


# ====== Main Script ======

# Choose which test to run
test_key = "large"  # Options: small, medium, large, set_small, set_medium, set_large, example
tree_file, label_file = TEST_FILES[test_key]
check_validity = False
save = False
main(test_key, tree_file, label_file, check_validity, save)

