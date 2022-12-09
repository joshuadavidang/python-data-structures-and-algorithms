class Solution:

    def twoSums(self, nums, target):
        dict_data = {}
        for index, value in enumerate(nums):
            # print(index, value)
            key = target - value
            if key in dict_data:
                return [dict_data[key], index]
            else:
                dict_data[value] = index


list_data = [2, 7, 11, 15]
target_no = 18
result = Solution().twoSums(list_data, target_no)
print(result)
