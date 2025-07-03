class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def perform_operations(s):
            i = 0
            while i < len(s):
                letter = s[i]
                if letter == "#" and i == 0:
                    s = s[1::]
                
                elif letter == "#":
                    s = s[:i - 1] + s[i + 1::]
                    i -= 1
                else:
                    i += 1
                print(s)
            return s


        return perform_operations(s) == perform_operations(t)
        
        