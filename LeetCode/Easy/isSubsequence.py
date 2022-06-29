
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i = 0
        for c in t:
            if c == s[i]:
                i += 1
            if i >= len(s):
                break
        if i == len(s):
            return True
        return False

s = "ab"
t = "baab"
obj1 = Solution()
print(obj1.isSubsequence(s, t))

"""
class Solution(object):
    def isSubsequence(self, s, t):
        temp = ""
        for each_letter in t:
            if each_letter not in s:
                t = t.replace(each_letter, "")
        if len(t) > len(s):
            for i in range(len(s)):
                if s[i] in t:
                    temp += s[i]
                    t = t.replace(s[i], "")
            if s == temp:
                return True
        elif t == s:
            return True
        return False
"""

