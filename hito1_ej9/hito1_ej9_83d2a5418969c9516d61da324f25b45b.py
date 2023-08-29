#Sistema de Ecuaciones
num1 = float(input("Ingrese numero 1: "))
num2 = float(input("Ingrese numero 2: "))
num3 = float(input("Ingrese numero 3: "))
num4 = float(input("Ingrese numero 4: "))
num5 = float(input("Ingrese numero 5: "))
num6 = float(input("Ingrese numero 6: "))

det = num1*num5 - num2*num4

x = (num3 * num5 - num2 * num6)/det
y = (num1 * num6 - num3 * num4)/det

print("x=",x,"y=",y)
      