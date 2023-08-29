#Sistema de Ecuaciones
a = float(input('Ingresa un número: '))
b = float(input('Ingresa otro número: '))
c = float(input('Ingresa otro número: '))
d = float(input('Ingresa otro número: '))
e = float(input('Ingresa otro número: '))
f = float(input('Ingresa otro número: '))

x = (c * e - b * f) / (a * e - d * b)
y = (a * f - c * d) / (a * e - d * b)

print("x=",x)
print("y=",y)
