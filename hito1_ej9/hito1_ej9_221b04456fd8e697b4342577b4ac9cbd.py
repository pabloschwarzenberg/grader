#Sistema de Ecuaciones
print ("Para realizar el sistema de ecuaciones, asigne valores a las letras: ax+by=c, dx=ey=f")
a = int(input("Que valor desea que tome a?"))
b = int(input("Que valor desea que tome b?"))
c = int(input("Que valor desea que tome c?"))
d = int(input("Que valor desea que tome d?"))
e = int(input("Que valor desea que tome e?"))
f = int(input("Que valor desea que tome f?"))
y=(a*f-d*c)/(a*e-d*b)
x=(c-b*y)/a
print("x=",x)
print("y=",y)
