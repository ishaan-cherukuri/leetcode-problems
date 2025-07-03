class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([token[::-1] for token in s.split()])