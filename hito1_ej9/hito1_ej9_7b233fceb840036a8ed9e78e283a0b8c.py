#Sistema de Ecuaciones
num1 = int(input("ingrese el primer numero:"))
num2 = int(input("ingrese el segundo numero:"))
num3 = int(input("ingrese el tercero numero:"))
num4 = int(input("ingrese el cuarto numero:"))
num5 = int(input("ingrese el quinto numero: "))
num6 = int(input("ingrese el sexto numero:"))
A = num1*num5-num2*num4
if A!=0:
    x_1=num5*num3-num2*num6
    x=round(x_1/A,1)
    y_1=num1*num6-num4*num3
    y=round(y_1/A,1)
    print("x=",x)
    print("y=",y)