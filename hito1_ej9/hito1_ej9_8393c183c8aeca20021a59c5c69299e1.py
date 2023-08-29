#Sistema de Ecuaciones
num1 = int(input("Ingrese el primer numero "))
num2 = int(input("Ingrese el segundo numero "))
num3 = int(input("Ingrese el tercer numero "))
num4 = int(input("Ingrese el cuarto numero "))
num5 = int(input("Ingrese el quinto numero "))
num6 = int(input("Ingrese el sexto numero "))

formula = (num1*num5) - (num2*num4)

x = ((num3*num5) - (num2*num6))/formula
y = ((num1*num6) - (num3*num4))/formula

print("x=",x,"y=",y)      