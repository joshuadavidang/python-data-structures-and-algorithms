def bubble_sort(data):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                is_sorted = False
                data[i], data[i + 1] = data[i + 1], data[i]
    return data


arr = [64, 34, 25, 12, 22, 11, 100, 90]
print(bubble_sort(arr))