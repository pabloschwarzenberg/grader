#Sistema de Ecuaciones
print("sistema de dos ecuaciones con dos incognitas")
a = int(input()) 
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

detS = (a*e)-(b*d)
detX = (c*e)-(b*f)
detY = (a*f)-(c*d)
print(detS)
print(detX)
print(detY)

x = detX/detS
y = detY/detS
print("[x={},y={}]".format(x,y))