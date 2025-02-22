
def selection_sort(arr):
    # Get the length of the array
    n = len(arr)
    # Traverse through all array elements
    print(f"Initial state: {arr}")
    for start_element in range(n):
        # Iterate through the array starting from the current start element
        min_element_index = start_element
        for current_element in range(start_element, n):
            # If the current element is less than current minimum element,
            # update the minimum element index
            if arr[current_element] < arr[min_element_index]:
                min_element_index = current_element
        arr[start_element], arr[min_element_index] = arr[min_element_index], arr[start_element]
        print(f"Current stage: {arr}")
    return arr
        
        
print(selection_sort([7, 5, 1, 8, 3]))