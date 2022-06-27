class Solution(object):
    def minPartitions(self, n):
        for i in range(9, -1, -1):
            if str(i) in n:
                return i
obj1 = Solution()
print(obj1.minPartitions(410323))

"""
        n = str(n)
        default = 0
        for each_num in n:
            if int(each_num) > default:
                default = int(each_num)
        return default
"""