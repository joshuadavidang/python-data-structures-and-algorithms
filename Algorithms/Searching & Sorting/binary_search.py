# 5 October 2022
# Algorithm - Binary Search

def binary_search(array, target):
    first = 0  # first element in the array
    last = len(array) - 1  # last element in the array

    while first <= last:
        mid_point = (first + last) // 2
        if array[mid_point] == target:
            # target found
            return mid_point

        elif array[mid_point] < target:
            # ignore values on the left, iterate forward
            first = mid_point + 1

        elif array[mid_point] > target:
            # ignore values on the right, iterate backwards
            last = mid_point - 1

    return None

customer_id = [2, 3, 7, 9, 12, 13]
find_id = binary_search(customer_id, 12)
print(f"Index of the target is at position {find_id}")
