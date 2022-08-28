# Merge Sort

def merge_sort(array):
    """
    Sorts a list in ascending order
    Returns a new sorted array

    Step 1:
       Divide: Find the midpoint of the array and divide into sub-array

    Step 2:
        Conquer: Recursively sort the sub-array created in previous step

    Step 3:
        Combine: Merge the sorted sub-array created in previous step

    A recursive function has a pattern.
    Base Case: a stopping condition.
    Stopping condition is our end goal, a sorted array.
    Come out with a simplest condition that satisfies this,
    A single array or empty array is naively sorted.
    """

    # Stopping Condition
    if len(array) <= 1:
        return array

    # Splits array into 2 sub-array, split is not a in-built function.
    left_half, right_half = split(array)

    # Sorts sub-array and returns it recursively
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    # Once 2 sub-array is sorted, we can combine it
    return merge(left, right)


def split(array):
    """
    Divide unsorted array at the midpoint, into sub-array
    Returns two sub-array - left and right

    Sample array
    array = [4, 2, 5, 1, 3, 6]
    """
    mid_point = len(array) // 2  # 3
    left = array[:mid_point]  # [4, 2, 5]
    right = array[mid_point:]  # [1, 3, 6]
    return left, right


def merge(left, right):
    """
    Merge two sub-array, sort them in the process
    Returns a new merged array
    """

    sorted_array = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array


customer_id = [4, 2, 5, 1, 3, 6]
print(f"Original array is {customer_id}")
sorted_version = merge_sort(customer_id)
print(f"Sorted array is {sorted_version}")
