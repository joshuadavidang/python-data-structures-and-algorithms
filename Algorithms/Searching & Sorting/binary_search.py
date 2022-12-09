class Algorithms:
    def binary_search(self, data, target):
        first_index = 0
        last_index = len(data) - 1

        while first_index < last_index:
            mid_point = (first_index + last_index) // 2
            if data[mid_point] == target:
                return mid_point

            elif data[mid_point] < target:
                # ignore values on the left, iterate forward
                first_index = mid_point + 1

            elif data[mid_point] > target:
                # ignore values on the right, iterate backwards
                last_index = mid_point - 1

        return -1


customer_id = [2, 3, 7, 9, 12, 13]
find_id = Algorithms().binary_search(customer_id, 12)
print(f"Index of the target is at position {find_id}")
