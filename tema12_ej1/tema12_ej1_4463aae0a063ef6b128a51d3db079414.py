def binaries_to1(num):
    global nums
    global j
    global p
    p+=1
    numb1=to1(num)
    if numb1 not in nums:
        nums.append(numb1)
    if p<=j:
        binaries_to1(nums[-1])
    else:
        return nums

def binaries_to0(num):
    global nums
    global j
    global p
    p+=1
    numb0=to0(num)
    if numb0 not in nums:
        nums.append(numb0)
    if p<=j:
        binaries_to1(nums[-1])
    else:
        return nums
    
def to1(numb):
    num=list(numb)
    num.reverse()
    for i in range(len(num)):
        if num[i]=='0':
            num[i]='1'
            break
    num.reverse()
    num="".join(num)
    return num

def to0(numb):
    num=list(numb)
    num.reverse()
    for i in range(len(num)):
        if num[i]=='1':
            num[i]='0'
            break
    num.reverse()
    num="".join(num)
    return num

n=int(input())
nums=['0'*n]
j=0
for k in nums[0]:
   if  k=='0':
       j+=1
p=0
binaries_to1(nums[0])
for no in nums:
    j=0
    for k in no:
        if  k=='0':
            j+=1
    p=0
    binaries_to0(no)

for nu in nums:
    print(nu)