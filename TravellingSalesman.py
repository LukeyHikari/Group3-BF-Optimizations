import itertools

# Brute-force TSP solution 
def brute_force_tsp(cost_matrix):
    n = len(cost_matrix)
    min_cost = float('inf')
    best_route = []
    print("Brute-force TSP: Evaluating all permutations...")

    for count, perm in enumerate(itertools.permutations(range(n)), start=1):
        cost = sum(cost_matrix[perm[i]][perm[(i + 1) % n]] for i in range(n))
        route_names = node_names(perm)
        print(f"Pass {count}: Route {route_names} Cost = {cost}")
        
        if cost < min_cost:
            min_cost = cost
            best_route = perm

    return best_route, min_cost

# Group Merging TSP algorithm 
def group_merging_tsp(cost_matrix):
    n = len(cost_matrix)
    
    groups = [[i] for i in range(n)]  # Each node is its own group
    step = 0

    print("Group Merging TSP: Starting with groups:")
    print_groups(groups)
    print()

    while len(groups) > 1:
        best_merge_cost = float('inf')
        best_pair = (None, None)
        best_order = None
        
        # Find the best merge
        for i in range(len(groups)):
            for j in range(len(groups)):
                if i != j:
                    # Merge in both possible orders because graph is undirected
                    for order in [(i, j), (j, i)]:
                        g1, g2 = groups[order[0]], groups[order[1]]
                        merge_cost = calculate_merge_cost(g1, g2, cost_matrix)
                        
                        if merge_cost < best_merge_cost:
                            best_merge_cost = merge_cost
                            best_pair = (order[0], order[1])
                            best_order = order
        
        # Merge the best pair of groups
        g1, g2 = groups[best_pair[0]], groups[best_pair[1]]
        new_group = g1 + g2  # Merge groups in order
        
        step += 1
        print(f"Pass {step}: Merging groups {node_names(g1)} and {node_names(g2)} with cost {best_merge_cost:.2f}")
        
        groups.append(new_group)  # Add new group
        
        # Remove the original two groups (remove by higher index first)
        groups.pop(max(best_pair))
        groups.pop(min(best_pair))

        print(f"Groups after merge {step}:")
        print_groups(groups)
        print()

    # Calculate total cost of the final route (including return to start)
    final_group = groups[0]
    total_cost = sum(cost_matrix[final_group[i]][final_group[(i + 1) % n]] for i in range(n))
    
    return final_group, total_cost

# Calculate merge cost with shape penalty heuristic
def calculate_merge_cost(g1, g2, cost_matrix):
    # Distance cost (cost between the last node of g1 and first node of g2)
    distance_cost = cost_matrix[g1[-1]][g2[0]]
    
    # Shape penalty calculation
    shape_penalty = 0
    if len(g1) > 1 and len(g2) > 1:
        penultimate_node = g1[-2]
        last_node = g1[-1]
        first_node = g2[0]
        second_node = g2[1]
        
        # Sum of costs of edges forming the angle
        shape_penalty = cost_matrix[penultimate_node][last_node] + cost_matrix[last_node][first_node]
    
    return distance_cost + 0.2 * shape_penalty  # Weight factor 0.2

def print_groups(groups):
    for idx, group in enumerate(groups):
        print(f"  Group {idx+1}: {node_names(group)}")

# Example undirected weighted graph cost matrix (symmetric)
# Nodes: A=0, B=1, C=2, D=3, E=4
example_cost_matrix = [
    #A  B   C   D   E
    [0, 47, 25, 33, 41],  # A
    [39, 0, 18, 44, 36],  # B
    [29, 17, 0, 22, 49],  # C
    [45, 39, 20, 0, 27],  # D
    [32, 40, 28, 34, 0],  # E
]

def node_names(route):
    mapping = ['A', 'B', 'C', 'D', 'E']
    return [mapping[i] for i in route]

#MAIN
print("=== Group Merging TSP ===")
merged_route, merged_cost = group_merging_tsp(example_cost_matrix)
print(f"Final Route: {node_names(merged_route)}")
print(f"Total Cost: {merged_cost:.2f}")

print("\n=== Brute-force TSP ===")
brute_route, brute_cost = brute_force_tsp(example_cost_matrix)
print(f"Optimal Route: {node_names(brute_route)}")
print(f"Minimal Cost: {brute_cost:.2f}")