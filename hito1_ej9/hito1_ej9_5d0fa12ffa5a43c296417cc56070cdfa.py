num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
num3 = int(input("ingrese el tercero numero: "))
num4 = int(input("ingrese el cuarto numero: "))
num5 = int(input("ingrese el quinto numero: "))
num6 = int(input("ingrese el sexto numero: "))

a = (num6*num1)-(num4*num3)
b = (num1*num5)-(num4*num2)

resultadoy = a/b

c = num3-num2*resultadoy
d = num1

resultadox = c/d

resultadoy = round(resultadoy,1)
resultadox = round(resultadox,1)

print('x=',resultadox)
print('y=', resultadoy)