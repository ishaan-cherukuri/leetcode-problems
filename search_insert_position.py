class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = []
        second = float('-inf')
        
        for num in nums[::-1]:
            if num < second:
                return True
            while stack and num > stack[-1]:
                second = stack.pop()
            stack.append(num)      
        return False