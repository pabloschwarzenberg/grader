#Sistema de Ecuaciones
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
num3 = int(input("ingrese el tercero numero: "))
num4 = int(input("ingrese el cuarto numero: "))
num5 = int(input("ingrese el quinto numero: "))
num6 = int(input("ingrese el sexto numero: "))

a = (num6*num1)-(num4*num3)
b = (num1*num5)-(num4*num2)

Y = a/b

c = num3-num2*Y
d = num1

X = c/d

Y = round(Y,1)
X = round(X,1)

print('x=', X)
print('y=', Y)