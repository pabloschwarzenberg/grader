print("Considere un sistema de ecuaciones de la siguiente forma: ")
print("  ax + by = c  |")
print("  dx + ey = f  |")
print("----------------")

print("*Recuerde que los coeficientes pertenecen a los números reales*")

a=float(input("Inserte el coeficiente a: "))
b=float(input("Inserte el coeficiente b: "))
c=float(input("Inserte el coeficiente c: "))
d=float(input("Inserte el coeficiente d: "))
e=float(input("Inserte el coeficiente e: "))
f=float(input("Inserte el coeficiente f: "))

#arreglos del profe
discriminante=(a*e-b*d)
if(a//d==0) and(b//e==0) and(c//d==0):
    print("El sistema tiene infinitas soluciones.")
elif(a*e==b*d):
    print("No existe solución.")
else:
    x=((b*f-c*e)/(b*d-a*e))
    y=((a*f-c*d)/(a*e-b*d))

    print("x=",x)
    print("y=",y)