def merge_sort(arr: list, start=0, end=None):
    """
    Sorts an array using the merge sort algorithm.
    
    Merge sort is a divide-and-conquer algorithm that recursively divides the input array into two halves,
    sorts them separately, and then merges the sorted halves to produce a fully sorted array.
    The algorithm has three main steps:
    1. Divide the array into two halves
    2. Recursively sort the two halves
    3. Merge the sorted halves back together
    
    The merge works by treating the subarrays as piles and repeatedly choosing the smaler element
    from the top of the subarrays and appending it to the merged array until both halves are exausted.
    
    Time Complexity: O(n log n) in all cases
        - The array is divided into halves log n times.
        - Each division takes O(n) time to merge.
    
    Space Complexity: O(n)
        - Additional space is required for the temporary subarrays used during merging.
    
    Args:
        arr (list): Array to be sorted
        start (int, optional): Starting index for the sort. Defaults to 0.
        end (int, optional): Ending index for the sort. Defaults to length of array.
    """
    if end is None:
        end = len(arr)
        
    # Base case: if subarray has more than one element
    if(end - start > 1):
        middle = (end + start) // 2
        # If the length is bigger than one, split the array in half, then call
        # recursively call sort on each half.
        merge_sort(arr, start, middle)
        merge_sort(arr, middle, end)
        # Merge the sorted halves
        merge(arr, start, middle, end)
        
def merge(arr, start, middle, end):
    """
    Merges two sorted subarrays into a single sorted array.
    
    Args:
        arr: The array containing the two sorted subarrays
        start: Starting index of first subarray
        middle: Starting index of second subarray
        end: End index of second subarray
    
    Time Complexity: O(n)
        - Each element is processed once during the merge.
    
    Space Complexity: O(n)
        - Additional space is required for the temporary subarrays used during merging.
    """
    print(f"Current state: {arr}")
    # Create left and right subarrays
    left_arr = arr[start:middle]
    right_arr = arr[middle:end]

    # The arrays will be merged like two deck of cards, where the smaller of the
    # current top elements of each array will be the next element of the merged
    # array
    left_top, right_top = 0, 0
    for k in range(start, end):
        # If left subarray is exhausted, take from right
        if left_top >= len(left_arr):
            arr[k] = right_arr[right_top]
            right_top += 1
        # If right subarray is exhausted, take from left
        elif right_top >= len(right_arr):
            arr[k] = left_arr[left_top]
            left_top += 1
        # If the current left array top is bigger than current right array top,
        # insert the current right array top in the position k of the sorted array.
        # Else, insert the current left array top in the position k of the sorted
        # array.
        elif left_arr[left_top] > right_arr[right_top]:
            arr[k] = right_arr[right_top]
            right_top += 1
        else:
            arr[k] = left_arr[left_top]
            left_top += 1
    

arr = [1, 2, 3, 4, 5, 6, 7, 8]
arr.reverse()
merge_sort(arr)
print(f"Final state: {arr}")