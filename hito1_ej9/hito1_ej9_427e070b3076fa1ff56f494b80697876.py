x0 = int(input("introduzca el x: "))
y0 = int(input("introduzca el y: "))
n0 = int(input("introduzca el n1: "))
x1 = int(input("introduzca el x2: "))
y1 = int(input("introduzca el y2: "))
n1 = int(input("introduzca el n2: "))

a = (n1*x0)-(x1*n0)
b = (x0*y1)-(x1*y0)
p2 = a/b

c = n0-y0*p2
d = x0
p1 = c/d

p2 = round(p2,1)
p1 = round(p1,1)

print('x=',p1)
print('y=', p2)