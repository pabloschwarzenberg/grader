k=int(input())
l=int(input())
m=int(input())
o=int(input())
q=int(input())
p=int(input())

A=k*q-l*o
if A!=0:
    x_1=q*m-l*p
    x=round(x_1/A,1)
    y_1=k*p-o*m
    y=round(y_1/A,1)
    print("x=",x)
    print("y=",y)
      