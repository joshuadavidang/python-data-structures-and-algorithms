def bubble_sort(list_a):

    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(len(list_a) - 1):
            if arr[i] > arr[i + 1]:
                is_sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return list_a


arr = [64, 34, 25, 12, 22, 11, 100, 90]
print(bubble_sort(arr))
