def merge_two_sorted_arrays(arr1, arr2):
    merged = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged

def merge_k_sorted_arrays(arrays):
    if not arrays:
        return []
    while len(arrays) > 1:
        merged_arrays = []
        for i in range(0, len(arrays), 2):
            arr1 = arrays[i]
            arr2 = arrays[i + 1] if i + 1 < len(arrays) else []
            merged_arrays.append(merge_two_sorted_arrays(arr1, arr2))
        arrays = merged_arrays
    return arrays[0]

# Example usage
array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8]
array3 = [0, 9, 10, 11]
arrays = [array1, array2, array3]
print(merge_k_sorted_arrays(arrays))



#This algorithm has a time complexity of O(N*K), where N represents the total number of elements in all arrays and K represents the number of arrays. This occurs because we are combining arrays individually.
