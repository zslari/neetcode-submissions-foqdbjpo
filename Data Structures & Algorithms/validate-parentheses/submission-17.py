class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []

        hash_map = {')':'(','}':'{',']':'['}

        for i in s:
            if i in hash_map:
                if stack and hash_map[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        

        return True if not stack else False





                

        