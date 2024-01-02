def count(arr, plotting=False):
    if arr is None:
        return 0
    if min(arr) < 0:
        shift = abs(min(arr))
        arr = [val + shift for val in arr]
    return count_water(arr, plotting)


def get_index_of_next_barrier(number, index, arr):
    index_of_max = index + 1
    for i in range(index_of_max, len(arr)):
        if arr[i] >= number:
            return i
        if i == len(arr) - 1:
            return i
    return None


def estimate(start, end, array):
    base_number = min(array[start], array[end])
    index = start + 1
    total = 0
    while index <= end:
        partial_total = base_number - array[index]
        if partial_total > 0:
            total += partial_total
        index += 1
    return total


def descending_step_found(index, arr):
    if index == len(arr) - 1:
        return False
    if arr[index] > arr[index + 1]:
        return True
    else:
        return False


def count_water(arr, plotting):
    total, index = 0, 0
    while index < len(arr):
        if descending_step_found(index, arr):
            greater_index = get_index_of_next_barrier(number=arr[index], index=index, arr=arr)
            if greater_index is not None:
                total += estimate(index, greater_index, arr)
                index = greater_index
            else:
                index += 1
        else:
            index += 1

    return total
