def selection_sort(arr : list):
    """
    Sorts an array using selection sort algorithm.
    
    Selection sort works by repeatedly finding the minimum element from the unsorted portion
    and placing it at the just after the sorted portion then increasing the sorted portion by one.
    
    Time Complexity: O(n^2) in all cases
        - due to the nested loops iterating over the array.
    
    Space Complexity: O(1) in all cases
        - as it sorts the array in place.
    
    Args:
        arr (list): Array to be sorted
    """
    # Length of array to sort
    n = len(arr)
    
    print(f"Initial state: {arr}")
    
    # Outer loop: defines the boundary between sorted and unsorted portions
    for start_element in range(n):
        # Assume current position contains minimum element
        min_element_index = start_element
        
        # Inner loop: find minimum element in unsorted portion
        for current_element in range(start_element, n):
            # Update minimum index if smaller element is found
            if arr[current_element] < arr[min_element_index]:
                min_element_index = current_element
        
        # Place minimum element at start of unsorted portion
        arr[start_element], arr[min_element_index] = arr[min_element_index], arr[start_element]
        print(f"Current stage: {arr}")
        
arr = [7, 5, 1, 8, 3]
selection_sort(arr)
print(f"Final array: {arr}")