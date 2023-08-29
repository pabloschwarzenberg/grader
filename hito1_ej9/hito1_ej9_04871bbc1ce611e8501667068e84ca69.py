#SISTEMA DE ECUACIONES

print("Ax+By=C")
print("Dx+Ey=F")

A=float(input("ingrese el valor de A en la primera ecuacion:"))
B=float(input("ingrese el valor de B en la primera ecuacion:"))
C=float(input("ingrese el valor de C en la primera ecuacion:"))
D=float(input("ingrese el valor de D en la segunda ecuacion:"))
E=float(input("ingrese el valor de E en la segunda ecuacion:"))
F=float(input("ingrese el valor de F en la segunda ecuacion:"))

n = A*E - B*D
if n != 0:
     x = (C*E - B*F)/n
     y = (A*F - C*D)/n
     print("x=",x)
     print("y=",y)
else:
     print("el sistema no tiene solucion")

      