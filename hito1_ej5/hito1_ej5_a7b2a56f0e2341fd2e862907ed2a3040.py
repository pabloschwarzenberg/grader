x=input()
a=(x[::-1])
b=((int(a[0])*2)+(int(a[1])*3)+(int(a[2])*4)+(int(a[3])*5))
e=((int(a[4])*6)+(int(a[5])*7)+(int(a[6])*2))
c=((b+e)%11)
d=(11-c)

if(float(10000000/int(a))<1):
    g=(int(x[0])*3)
    w=((b+e+g)%11)
    z=(11-w)
    
    if(z==10):
        print("dv=k")
    else:
        if(w==0):
           print("dv=0")
        else:
           print("dv=",z)

elif(float(10000000/int(a))>=1):
    if(d==10):
            print("dv=k")
    else:
        if(c==0):
            print("dv=0")
        else:
            print("dv=",d)


