nums=[]
nums.append(input(" "))
nums=str(nums)
if sum(1 for nums in nums if nums.isdigit())==4:
 print((nums[2] + "M") +"+"+ (nums[3] + "C") +"+"+ (nums[4] + "D") +"+"+ (nums[5] + "U"))
elif sum(1 for nums in nums if nums.isdigit())==3:
 print((nums[2] + "C") +"+"+ (nums[3] + "D") +"+"+ (nums[4] + "U"))
elif sum(1 for nums in nums if nums.isdigit())==2:
 print((nums[2] + "D") +"+"+ (nums[3] + "U"))
elif sum(1 for nums in nums if nums.isdigit())==1:
 print(nums[2] + "U")

 
