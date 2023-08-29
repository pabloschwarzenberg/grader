ing=str(input())
ex=2
delta=0
for i in range(len(ing)):
    if ex<8:
       delta+=int(ing[i])*ex
       ex=ex+1
    else:
        delta+=int(ing[i])*2
        ex=3
alfa=delta%11
res=delta-(11*alfa)
res1=11-res
if res1==11:
    print('dv=',0)
elif res1==10:
    print('dv=k')
else:
    print('dv=',res1)