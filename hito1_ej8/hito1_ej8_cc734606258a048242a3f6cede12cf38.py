num=str(input())
alfa=len(num)
res=''
M=''
C=''
D=''
U=''
for i in range(alfa):
    if i==0:
       U=num[alfa-1]+'U'
    elif i==1:
       D=num[alfa-2]+'D'
    elif i==2:
       C=num[alfa-3]+'C'
    elif i==3:
       M=num[alfa-4]+'M'
res=M+'+'+C+'+'+D+'+'+U
print(res)
