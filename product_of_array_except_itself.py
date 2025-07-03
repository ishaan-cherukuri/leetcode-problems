class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        forward = [1]
        current_sum = 1
        for num in nums:
            current_sum *= num
            forward.append(current_sum)

        backward = [1]
        current_sum = 1
        for num in nums[::-1]:
            current_sum *= num
            backward.append(current_sum)

        print(forward, backward)
        answer = [0] * len(nums)
        for i in range(len(nums)):
            answer[i] = forward[i] * backward[len(nums) - 1 - i]
        
        return answer
