#Sistema de Ecuaciones
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())

M=a*e-b*d
if M!=0:
    x_1=e*c-b*f
    X=round(x_1/M,1)
    y_1=a*f-d*c
    Y=round(y_1/M,1)
    print("x=",X)
    print("y=",Y)



    
      