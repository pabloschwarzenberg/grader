num1 = int(input("Ingresa primero numero: "))
num2 = int(input("Ingresa segundo numero: "))
num3 = int(input("Ingresa tercer numero: "))
num4 = int(input("Ingresa cuarto numero: "))
num5 = int(input("Ingresa quinto numero: "))
num6 = int(input("Ingresa sexto numero: "))

num1, num4, num2, num5, num3, num6 = num1*num4, num4*num1, num2*num4, num5*num1, num3*num4, num6*num1

y = (num3 - num6)/(num2 - num5)

x = (num3 - (num2 * y))/num1

print("x="+str(x))
print("y="+str(y))