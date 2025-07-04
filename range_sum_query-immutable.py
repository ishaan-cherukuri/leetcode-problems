class NumArray:

    def __init__(self, nums: list[int]):
        obj = nums
        self.prefix = [0] * (len(obj) + 1)
        for i in range(1, len(obj) + 1):
            self.prefix[i] = self.prefix[i - 1] + obj[i - 1]
        print(self.prefix)
    def sumRange(self, left: int, right: int) -> int:
        return (self.prefix[right + 1]) - (self.prefix[left])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)