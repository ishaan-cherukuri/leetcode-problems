class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        new_nums = {nums[i]: i for i in range(0, n)}
        print(new_nums)
        print()
        for i in range(n):
            diff = target - nums[i]
            print(diff)
            if diff in new_nums and new_nums[diff] != i:
                return [new_nums[diff], i]
        
        return
        