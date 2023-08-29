#Nota final
pt=float(input("Ingrese las nota de tareas :"))
pi=float(input("Ingrese las nota de interrogaciones :"))
ne=float(input("Ingrese las nota de examen:"))
pp=float(input("Ingrese las notas de presentacion :"))
calculo=  (0.3*pt) + (0.3*pi)+ (0.3*ne) + (0.1*pp)
print("Su promedio final es :",round(calculo,1))