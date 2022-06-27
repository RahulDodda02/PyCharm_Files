class solution():
    def twosum(self, nums, target):
        required = {}
        for i in range(len(nums)):
            if target - nums[i] in required:
                return [required[target - nums[i]],i]
            else:
                required[nums[i]] = i

input_list = [1,3,7,13,18]
target = 20
obj1 = solution()
print(obj1.twosum(input_list,target))

