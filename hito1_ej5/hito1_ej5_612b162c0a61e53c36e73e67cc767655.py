#Cálculo del dígito verificador de un rut
n=int(input())
a=(str(n)[::-1])
l=len(a)
if l==8:
    a1=int(a[:1])*2
    a2=int(a[1:2])*3
    a3=int(a[2:3])*4
    a4=int(a[3:4])*5
    a5=int(a[4:5])*6
    a6=int(a[5:6])*7
    a7=int(a[6:7])*2
    a8=int(a[7:8])*3

else:
    a1=int(a[:1])*2
    a2=int(a[1:2])*3
    a3=int(a[2:3])*4
    a4=int(a[3:4])*5
    a5=int(a[4:5])*6
    a6=int(a[5:6])*7
    a7=int(a[6:7])*2
if l==8:
    b=int(a1+a2+a3+a4+a5+a6+a7+a8)
    c=int(b//11)
    d=int(b-(11*c))
    e=int(11-d)
else:
    b=int(a1+a2+a3+a4+a5+a6+a7)
    c=int(b//11)
    d=int(b-(11*c))
    e=int(11-d)

if e==11:
    print("dv=0")
elif e==10:
    print("dv=k")
else:
    print("dv=",e)

      