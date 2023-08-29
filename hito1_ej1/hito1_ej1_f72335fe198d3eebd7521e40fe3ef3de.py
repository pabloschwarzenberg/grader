#Nota final

a=float(input("Ingrese su nota de Tareas :"))
b=float(input("Ingrese su nota de Interrogación :"))
c=float(input("Ingrese su nota de Examen :"))
d=float(input("Ingrese su nota de Presentación :"))

e=round((0.3*(a+b+c)+0.1*d),1)


print("su promedio final es :", e)