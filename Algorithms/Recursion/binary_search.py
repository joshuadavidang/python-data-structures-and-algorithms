def recursive_binary_search(array, target):
    if len(array) == 0:
        return False

    else:
        mid_point = len(array) // 2

        if array[mid_point] == target:
            return True
        else:
            if array[mid_point] < target:
                # from mid-point to the end of the array
                return recursive_binary_search(array[mid_point+1:], target)
            else:
                return recursive_binary_search(array[:mid_point], target)


customer_id = [2, 3, 7, 9, 12, 13]
search_for_id = recursive_binary_search(customer_id, 12)
print(f"Target found? {search_for_id}")
