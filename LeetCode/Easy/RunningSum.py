class Solution(object):
    def runningSum(self, nums):
        current = 0
        running = []
        for each_num in nums:
            current += each_num
            running.append(current)
        return running

nums = [1,2,3,4,7,12]
obj1 = Solution()
print(obj1.runningSum(nums))

