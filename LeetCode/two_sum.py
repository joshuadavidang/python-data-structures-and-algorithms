class Solution:

    def twoSums(self, nums, target):
        values = {}
        for index, value in enumerate(nums):
            print(id, value)
            remaining = target - value
            if remaining in values:
                return [values[remaining], index]
            else:
                values[value] = index


list_data = [2, 7, 11, 15]
target_no = 9
result = Solution().twoSums(list_data, target_no)
print(result)
