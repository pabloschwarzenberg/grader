#Sistema de Ecuaciones
A= float(input())
B= float(input())
C= float(input())
D= float(input())
E= float(input())
F= float(input())

def function():
    v1= E*(-A) + B*(D)
    v2= F*(-A) + C*(D)
    y= v2/v1
    x= (C-(B*y))/A

    print("x=",x)
    print("y=",y)

function()