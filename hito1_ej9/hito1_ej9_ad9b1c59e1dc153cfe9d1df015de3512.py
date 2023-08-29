#Sistema de Ecuaciones
print("El programa resolvera las siguientes ecuaciones:")
print("2x + 3y = 6 que la representaremos como ax + by = c")
print("1x + 2y = 5 que la representaremos como dx + ey = f")

a = int(input("ingrese el numero 2: "))
b = int(input("ingrese el numero 3: "))
c = int(input("ingrese el numero 6: "))
d = int(input("ingrese el numero 1: "))
e = int(input("ingrese el numero 2: "))
f = int(input("ingrese el numero 5: "))

y = ((a*f)-(d*c))/((a*e)-(d*b))
x = (f-(e*y))/d
print("y= ",y)
print("x= ",x)
      