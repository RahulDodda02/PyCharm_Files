class Solution(object):
    def isValid(self, s):
        if len(s) % 2 != 0:
            return False
        pairs = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for i in s:
            if i in pairs.keys():
                stack.append(i)
            else:
                if not stack:
                    return False
                a = stack.pop()
                if i != pairs[a]:
                    return False
        return stack == []

pars = "({}([])}"
obj1 = Solution()
print(obj1.isValid(pars))
