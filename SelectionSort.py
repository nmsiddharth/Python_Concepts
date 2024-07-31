nums = [4,6,2,3,8,7]

# Selection sort avoids swapping multiple times in iteration, it only swaps one time
def sort(nums):
    for i in range(len(nums)):
        min = i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[min]:
                min = j
        nums[i],nums[min] = nums[min],nums[i]
        print(nums)

sort(nums)