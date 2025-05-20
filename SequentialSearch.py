def sequential_search_even_odd(arr, target):
    # Print the array and target value
    print(f"Searching for {target} in the array: {arr}")

    # First pass: search in even indexes (0, 2, 4, ...)
    print("\nChecking even indexes:")
    i = 0
    while i < len(arr):
        # Show current index and value
        print(f"Comparing with element at index {i}: {arr[i]}")
        # Check if the element matches the target
        if arr[i] == target:
            print(f"Element found at even index {i}")
            return i
        # Move to the next even index
        i += 2

    # Second pass: search in odd indexes (1, 3, 5, ...)
    print("\nChecking odd indexes:")
    i = 1
    while i < len(arr):
        # Show current index and value
        print(f"Comparing with element at index {i}: {arr[i]}")
        # Check if the element matches the target
        if arr[i] == target:
            print(f"Element found at odd index {i}")
            return i
        # Move to the next odd index
        i += 2

    # If target not found in either pass
    print("Element not found in the array.")
    return -1


# Example usage of the function
arr = [10, 23, 45, 70, 11, 15, 30, 22]  # Sample array
target = 15                             # Target to find
sequential_search_even_odd(arr, target)