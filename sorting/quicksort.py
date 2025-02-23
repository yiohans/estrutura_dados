def quick_sort(arr: list, start=0, end=None):
    """
    Sorts an array using the quick sort algorithm.
    
    Quick sort is a divide-and-conquer algorithm that selects a pivot element from the array,
    partitions the other elements into two subarrays according to whether they are less than or greater than the pivot,
    and then recursively sorts the subarrays.
    
    Time Complexity: O(n log n) on average, O(n^2) in the worst case.
        - On average, the array is divided into two halves log n times.
        - Each division takes O(n) time to partition.
    
    Space Complexity: O(log n) due to the recursion stack.
        - The depth of the recursion stack is log n on average.
    
    Args:
        arr (list): Array to be sorted
        start (int, optional): Starting index for the sort. Defaults to 0.
        end (int, optional): Ending index for the sort. Defaults to length of array minus one.
    """
    # Set the variable end if it is not passed
    if end == None:
        end = len(arr)-1
    # If start is less than end, find the pivot index using partition function,
    # then recursively sort the subarrays before and after the pivot
    print(f"Current state: {arr}")
    if start < end:
        pivot_index = partition(arr, start, end)
        quick_sort(arr, start, pivot_index-1)
        quick_sort(arr, pivot_index+1, end)
        
def partition(arr: list, start: int, end: int) -> int:
    """
    Partitions the array into two subarrays based on a pivot element.
    
    Elements less than the pivot are moved to the left of the pivot,
    and elements greater than the pivot are moved to the right of the pivot.
    
    Args:
        arr (list): The array to be partitioned
        start (int): Starting index of the subarray to be partitioned
        end (int): Ending index of the subarray to be partitioned
    
    Returns:
        int: The index of the pivot element after partitioning
    
    Time Complexity: O(n)
        - Each element is processed once during the partition.
    
    Space Complexity: O(1)
        - No additional space is required beyond the input array.
    """
    # Start with the first element as the boundary between smaller and bigger elements
    smaller_end_index = start
    # Iterate through array (except last element which is the pivot)
    for bigger_end_index in range(start, end):
        # If current element is smaller than pivot, swap it with element at
        # smaller_end_index and increment smaller_end_index
        if arr[bigger_end_index] < arr[end]:
            arr[smaller_end_index], arr[bigger_end_index] = arr[bigger_end_index], arr[smaller_end_index]
            smaller_end_index += 1
    # Place pivot in its final position by swapping with element at smaller_end_index
    arr[smaller_end_index], arr[end] = arr[end], arr[smaller_end_index]
    return smaller_end_index
    
arr = [4, 7, 2, 6, 4, 1, 8, 3]

quick_sort(arr)

print(arr)