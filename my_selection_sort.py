def selection_sort(arr):
    for i in range(len(arr)):
        #find the min element in the remaining unsorted portion of the array
        min_index = i 
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]: 
                min_index = j
        # Swap the found minimum element with the element at index i
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([3, -1, 5, 2]))  # Expected output: [-1, 2, 3, 5]