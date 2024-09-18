def remove_duplicates(array):
    if not array:
        return []

    seen = set()
    result = []
    for num in array:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result
array = [1, 2, 2, 3, 4, 4, 4, 5, 5]
print(remove_duplicates(array))

#This algorithm has a time complexity of O(N), with N representing the total number of elements in the array. This occurs because we iterate through the array only once.