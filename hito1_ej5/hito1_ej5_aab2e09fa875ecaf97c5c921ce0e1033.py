d=sum([int(n)*(i%6+2)for i,n in enumerate(input()[::-1])])%11
if d==1:
    print("dv=k")
elif d==0:
    print("dv=",0)
else:
    print("dv=",11-d)
