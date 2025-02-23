
def selection_sort(arr):
    # Get the length of the array
    n = len(arr)
    # Increase the start position when the minimum element is found and swaped
    # with the element in the current start position
    print(f"Initial state: {arr}")
    for start_element in range(n):
        # Iterate through the array starting from the current start element
        min_element_index = start_element
        for current_element in range(start_element, n):
            # If the current element is less than current minimum element,
            # update the minimum element index
            if arr[current_element] < arr[min_element_index]:
                min_element_index = current_element
        # Swap the current start position and minimum elements
        arr[start_element], arr[min_element_index] = arr[min_element_index], arr[start_element]
        print(f"Current stage: {arr}")
        
arr = [7, 5, 1, 8, 3]
selection_sort(arr)
print(f"Final array: {arr}")