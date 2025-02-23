
def merge(arr, inicio, meio, fim):
    print(f"Current state: {arr}")
    # Extract an array from the elements from start until the middle position
    # minus one and call it left array
    arr_esq = arr[inicio:meio]
    # Extract an array from the elements from middle until the last position
    # minus one and call it right array
    arr_dir = arr[meio:fim]
    # The arrays will be merged like two deck of cards, where the smaller of the
    # current top elements of each array will be the next element of the merged
    # array
    topo_esq, topo_dir = 0, 0
    for k in range(inicio, fim):
        # If the current top index one of the decks is bigger than the array,
        # only use the other array
        if topo_esq >= len(arr_esq):
            arr[k] = arr_dir[topo_dir]
            topo_dir += 1
        elif topo_dir >= len(arr_dir):
            arr[k] = arr_esq[topo_esq]
            topo_esq += 1
        # If the current left array top is bigger than current right array top,
        # insert the current right array top in the position k of the sorted array.
        # Else, insert the current left array top in the position k of the sorted
        # array.
        elif arr_esq[topo_esq] > arr_dir[topo_dir]:
            arr[k] = arr_dir[topo_dir]
            topo_dir += 1
        else:
            arr[k] = arr_esq[topo_esq]
            topo_esq += 1
    
    
def merge_sort(arr : list, inicio=0, fim=None):
    # Set the variable end if it is not passed
    if fim is None:
        fim = len(arr)
    # If the length is bigger than one, split the array in half, then call
    # merge_sort on each half. After that, call merge to merge the sorted
    # half-arrays into an array of the original length
    if(fim - inicio > 1):
        meio = (fim + inicio) // 2
        merge_sort(arr, inicio, meio)
        merge_sort(arr, meio, fim)
        merge(arr, inicio, meio, fim)

arr = [1, 2, 3, 4, 5, 6, 7, 8]
arr.reverse()
merge_sort(arr)
print(f"Final state: {arr}")