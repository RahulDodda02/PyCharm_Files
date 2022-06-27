class Solution(object):
    def isIsomorphic(self, s, t):
        dct1 = {}
        dct2 = {}
        for c1, c2 in zip(s, t):
            if c1 not in dct1 and c2 not in dct2:
                dct1[c1] = c2
                dct2[c2] = c1
            elif dct1.get(c1) != c2 or c1 != dct2.get(c2):
                return False
        return True

