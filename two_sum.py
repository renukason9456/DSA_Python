'''Two Sum

Given an array and a target, find two numbers such that their sum equals the target.
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1].'''
def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]+nums[j] == target):
                return i,j
            else:
                print ("no data")


nums = [2, 7, 11, 15]
target = 9
list = two_sum(nums,target)
print(list)

