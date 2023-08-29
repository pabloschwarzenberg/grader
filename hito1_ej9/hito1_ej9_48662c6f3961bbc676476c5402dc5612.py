#Sistema de Ecuaciones
x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())

x = round((y2*r1 - y1*r2) / (y2*x1 - y1*x2), 1)

y = round((r1 - x1*x) / y1, 1)

print("x={}".format(x))
print("y={}".format(y))