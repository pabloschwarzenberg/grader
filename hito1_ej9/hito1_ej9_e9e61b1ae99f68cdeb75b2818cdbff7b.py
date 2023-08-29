#Sistema de Ecuaciones
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
num3 = int(input("ingrese el tercero numero: "))
num4 = int(input("ingrese el cuarto numero: "))
num5 = int(input("ingrese el quinto numero: "))
num6 = int(input("ingrese el sexto numero: "))

a = (num6*num1)-(num4*num3)
b = (num1*num5)-(num4*num2)

Ry = a/b

c = num3-num2*Ry
d = num1

Rx = c/d

Ry = round(Ry,1)
Rx = round(Rx,1)

print('x=',Rx)
print('y=', Ry)      