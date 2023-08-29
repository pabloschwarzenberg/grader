a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())

D=a*e-b*d
if D!=0:
    x_1=e*c-b*f
    x=round(x_1/D,1)
    y_1=a*f-d*c
    y=round(y_1/D,1)
    print("x=",x)
    print("y=",y)
      