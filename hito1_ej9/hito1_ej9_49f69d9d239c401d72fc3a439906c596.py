#Sistema de Ecuaciones
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

y = (c - (a * f)) / (a * (-e) + b)
x = f - (a * y)
x = 'x=' + str(x)
y = 'y=' + str(y)

print([x, y])
  