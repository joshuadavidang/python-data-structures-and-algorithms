class Search:
    def binary_search(self, data, target):

        left, right = 0, len(data) - 1

        while left <= right:

            mid = (left + right) // 2

            if data[mid] > target:
                right = mid - 1  # ignore values on the right, iterate backwards

            elif data[mid] < target:
                left = mid + 1  # ignore values on the left, iterate forward

            else:
                return mid  # target found

        return -1


customer_id = [2, 3, 7, 9, 12, 13]
find_id = Search()
result = find_id.binary_search(customer_id, 7)
print("Target: 7")
print(f"Index of the target is at position {result}")
