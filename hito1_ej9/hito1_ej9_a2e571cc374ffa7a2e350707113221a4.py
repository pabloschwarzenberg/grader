#Sistema de Ecuaciones
a1= float(input())
b1= float(input())
c1= float(input())

a2=float(input())
b2=float(input())
c2=float(input())

x = round((b2*c1-b1*c2)/(b2*a1-a2*b1), 1)
y = round((c1-a1*x)/b1, 1)
print("x="+str(x)+"y="+str(y))