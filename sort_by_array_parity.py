class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        def move(arr, new_index, old_index):
            if new_index >= len(arr):
                arr.extend([None] * (new_index - len(arr) + 1))
            arr.insert(new_index, arr.pop(old_index))
        
        i, j = 0, 0
        while j < len(nums):
            if nums[j] % 2 == 0:
                move(nums, i, j)
                i += 1
                j = i
            else:
                j += 1
        return nums