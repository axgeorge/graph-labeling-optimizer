
import numpy as np
from collections import deque 


def bfs(tree, root_node):

    track_visited = {}
    for node in range(len(tree)):
        track_visited[node] = 0 # unvisited

    visited = [root_node]
    queue = deque([root_node])
    track_visited[root_node] = 1
    while queue:
        current_node = queue.popleft()
        for node in tree[current_node]:
            if track_visited[node] == 0:
                visited.append(node)
                queue.append(node)
                track_visited[node] = 1
    return visited 


def closest_k_neighbors(tree, source_node, k, labeling):
    
    track_visited = {}
    for node in range(len(tree)):
        track_visited[node] = 0 # unvisited
    used_labels = []

    counter = 1 # First neighbor is the source node itself.
    k_closest = [source_node]
    queue = deque([source_node])
    track_visited[source_node] = 1
    if labeling[source_node] != -1:
        used_labels.append(labeling[source_node])
    while queue and counter < k:
        current_node = queue.popleft()
        for node in tree[current_node]:
            if track_visited[node] == 0:
                if counter < k:
                    counter += 1
                    k_closest.append(node)
                    queue.append(node)
                    track_visited[node] = 1
                    if labeling[node] != -1:
                        used_labels.append(labeling[node])
    
    return k_closest, used_labels 


def labeling_algorithm(tree, root_node, k):
    
    n = len(tree)
    labeling = [-1 for i in range(n)] # No valid labels assigned yet.
    visited = bfs(tree, root_node)
    
    for node in visited:
        k_closest, used_labels = closest_k_neighbors(tree, node, k, labeling)
        allowed_labels = deque([label for label in range(k) if label not in used_labels])
        for neighbor in k_closest:
            if labeling[neighbor] == -1:
                labeling[neighbor] = allowed_labels.popleft()   
    
    return labeling


# Define the checking functions.


def bellman_ford_shortest(source, subtree, tree):
    p = len(subtree)
    track_dist = {}
    for node in subtree:
        track_dist[node] = [np.inf, None] # Tuple (d(node),pi(node)).
    track_dist[source][0] = 0
    for i in range(p-1):
        for node in subtree:
            for neighbor in tree[node]:
                if neighbor in subtree:
                    if track_dist[node][0] + 1 < track_dist[neighbor][0]:
                        track_dist[neighbor][0] = track_dist[node][0] + 1
                        track_dist[neighbor][1] = node
    return track_dist


def closest_k_labels(tree, source_node, k, sol_labeling):
    
    track_visited = {}
    for node in range(len(tree)):
        track_visited[node] = 0 # unvisited
    klabels = [label for label in range(k)] # The k distict labels.

    k_closest = [source_node] # All nodes within smallest radius containing k distict labels.
    queue = deque([source_node])
    track_visited[source_node] = 1
    klabels.remove(sol_labeling[source_node])
    while queue and klabels: 
        current_node = queue.popleft()
        for node in tree[current_node]:
            if track_visited[node] == 0:
                if klabels:
                    k_closest.append(node)
                    queue.append(node)
                    track_visited[node] = 1
                    klabels.remove(sol_labeling[node])
    
    return k_closest


def find_proximity(tree, root_node, k, sol_labeling):
    ratios = []
    visited = bfs(tree, root_node)
    for node in visited:
        min_k_label_neighborhood = closest_k_labels(tree, node, k, sol_labeling)
        min_k_node_neighborhood, used_labels = closest_k_neighbors(tree, node, k, sol_labeling)
        dists_labels = bellman_ford_shortest(node, min_k_label_neighborhood, tree)
        dists_nodes = bellman_ford_shortest(node, min_k_node_neighborhood, tree)
        hops_labels = [dists_labels[nodes][0] for nodes in dists_labels]
        hops_nodes = [dists_nodes[nodes][0] for nodes in dists_nodes]
        # print("for node",node,"hops_labels =",hops_labels)
        # print("for node",node,"hops_nodes =",hops_nodes)
        r_node = max(hops_labels)
        m_node = max(hops_nodes)
        ratio = r_node/m_node
        ratios.append(ratio)
    max_ratio = max(ratios)
    return max_ratio


def check_validity(tree, k, sol_labeling):
    num_nodes = len(tree)
    num_labels = len(sol_labeling)
    if num_labels != num_nodes:
        print("VALIDITY ERROR: TREE HAS",num_nodes,"NODES, BUT SOL HAS",num_labels,"LABELS")
    for label in range(k):
        if label not in sol_labeling:
            print("VALIDITY ERROR: LABEL",label,"NOT IN SOL")
    for label in sol_labeling:
        if label < 0 or label > (k-1):
            print("VALIDITY ERROR: SOL HAS INVALID LABEL",label,"NOT IN RANGE ["+str(0)+", "+str(k-1)+"]")

