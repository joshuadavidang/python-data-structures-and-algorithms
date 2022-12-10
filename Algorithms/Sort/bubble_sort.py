class Sort:
    def bubble_sort(self, data):
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(len(data) - 1):
                if data[i] > data[i + 1]:
                    is_sorted = False
                    data[i], data[i + 1] = data[i + 1], data[i]
        return data


num_list = [64, 34, 25, 12, 22, 11, 100, 90]
res = Sort().bubble_sort(num_list)
print(res)