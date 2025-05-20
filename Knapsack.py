def knapsack_brute_force(capacity, n, values, weights):
    # print(f"knapsack_brute_force({capacity},{n})")
    # Base Case
    if n == 0 or capacity == 0:
        return 0
    # Proceed to next item if weight already exceeds item capacity
    elif weights[n-1] > capacity:
        return knapsack_brute_force(capacity, n-1, values, weights)
    # Check whether an item adds more value if it is included or excluded and proceed with the more valuable one
    else:
        include_item = values[n-1] + knapsack_brute_force(capacity-weights[n-1], n-1, values, weights)
        exclude_item = knapsack_brute_force(capacity, n-1, values, weights)
        return max(include_item, exclude_item)
    
def kp_dynamic_1D(capacity, item_count, values, weights):
    # Create a table based on the capacity of the  which has initial value 0
    table = [0] * (capacity+1)
    # Iterate over all items
    for i in range(item_count):
        # Iterate backward from the item list
        for w in range(capacity, weights[i] - 1, - 1):
            # Decide whether an item is included in the knapsack at current weight limit
            # Overwrites when the value is higher then removes that item from the table to avoid duplication
            table[w] = max(table[w],table[(w - weights[i])] + values[i])
    # Return the highest value found (the last value in the table)
    return table[capacity]
       
if __name__ == '__main__':
    item_values = [300, 200, 400, 500]
    item_weights = [2, 1, 5, 3]
    capacity = 10
    n = len(item_values)
    print("Maximum Knapsack Value for 1D Array Dynamic Programming = ", kp_dynamic_1D(capacity, n, item_values, item_weights))
    print("Maximum Knapsack Value for Brute Force =", knapsack_brute_force(capacity, n, item_values, item_weights))
