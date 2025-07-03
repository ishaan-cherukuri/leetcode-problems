from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        new_nums = defaultdict(int)

        for num in nums:
            new_nums[num] += 1

        ele = [{'num': num, 'count': count} for num, count in new_nums.items()]

        ele = sorted(ele, key=lambda x:x["count"])
        return [num['num'] for num in ele[len(ele) - k::]]