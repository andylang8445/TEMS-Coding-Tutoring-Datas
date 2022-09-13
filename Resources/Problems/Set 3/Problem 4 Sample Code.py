def searcher(original_list, data):
    left = 0
    right = len(original_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if original_list[mid] == data:
            return mid
        elif original_list[mid] < data:
            left = mid + 1
        else:
            right = mid - 1
    return -1