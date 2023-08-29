#Sistema de Ecuaciones
x1 = int(input())
y1 = int(input())
z1 = int(input())
x2 = int(input())
y2 = int(input())
z2 = int(input())
# x + y = z
# x1+y1=z1
# x2=z2-y2
# y
a = x1 * z2
b = x1 * (y2*-1)
c = b + y1
d = z1-a
e = d*-1
#x
f = z2 - y2 * e
print('x=',f)
print('y=',e)