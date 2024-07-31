nums = [4,6,2,3,8,7]


#def sort(nums):
 #   for i in range(len(nums)-1,0,-1):
  #      for j in range(i):
   #         if nums[j]>nums[j+1]:
    #            temp = nums[j]
     #           nums[j] = nums[j+1]
      #          nums[j+1] = temp
    #print(nums)
def sort(nums):
    for i in range(0,len(nums)-1):
        for j in range(0,len(nums)-1-i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    print(nums)

sort(nums)