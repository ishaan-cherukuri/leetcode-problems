class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        len_word_1 = len(word1)
        len_word_2 = len(word2)
        res = ""
        while True:
            if 0 <= i < len_word_1 and 0 <= j < len_word_2:
                res += word1[i] + word2[j]
                i += 1
                j += 1
            elif 0 <= i < len_word_1 and j == len_word_2:
                return res + word1[i::]
            elif i >= len_word_1 and 0 <= j < len_word_2:
                return res + word2[j::]
            else:
                return res