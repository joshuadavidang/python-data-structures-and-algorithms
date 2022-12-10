class Sort:
    def split(self, array):
        mid_point = len(array) // 2
        left = array[:mid_point]
        right = array[mid_point:]
        return left, right

    def merge(self, left, right):
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

    def merge_sort(self, array):
        if len(array) <= 1:
            return array

        left_half, right_half = Sort().split(array)

        left = Sort().merge_sort(left_half)
        right = Sort().merge_sort(right_half)

        return Sort().merge(left, right)


customer_id = [4, 2, 5, 1, 3, 6]
print(f"Original list {customer_id}")
sorted_version = Sort().merge_sort(customer_id)
print(f"Sorted list {sorted_version}")