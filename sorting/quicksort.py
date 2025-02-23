def quick_sort(arr, inicio=0, fim=None):
    # Set the variable end if it is not passed
    if fim == None:
        fim = len(arr)-1
    # If start is less than end, find the pivot index using partition function,
    # then recursively sort the subarrays before and after the pivot
    if inicio < fim:
        indice_pivo = partition(arr, inicio, fim)
        quick_sort(arr, inicio, indice_pivo-1)
        quick_sort(arr, indice_pivo+1, fim)
        
def partition(arr, inicio, fim):
    # Start with the first element as the boundary between smaller and bigger elements
    smaller_end_index = inicio
    # Iterate through array (except last element which is the pivot)
    for bigger_end_index in range(inicio, fim):
        # If current element is smaller than pivot, swap it with element at
        # smaller_end_index and increment smaller_end_index
        if arr[bigger_end_index] < arr[fim]:
            arr[smaller_end_index], arr[bigger_end_index] = arr[bigger_end_index], arr[smaller_end_index]
            smaller_end_index += 1
    # Place pivot in its final position by swapping with element at smaller_end_index
    arr[smaller_end_index], arr[fim] = arr[fim], arr[smaller_end_index]
    return smaller_end_index
    
arr = [4, 7, 2, 6, 4, 1, 8, 3]

quick_sort(arr)

print(arr)