class Solution(object):
    def pivotIndex(self, nums):
        startIndex = 0
        leftSum = 0
        rightSum = sum(nums) - nums[0]
        totLeftSum = sum(nums) - nums[len(nums) - 1]
        try:
            while leftSum != rightSum:
                startIndex += 1
                leftSum += nums[startIndex-1]
                rightSum -= nums[startIndex]
        except:
            startIndex = -1
        return startIndex


nums = [1,2,3]
obj1 = Solution()
print(obj1.pivotIndex(nums))

