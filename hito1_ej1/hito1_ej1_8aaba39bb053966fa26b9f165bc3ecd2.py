#Nota final
print("¡hola!, calcula tu promedio")


pt=input("ingrese su nota de tareas: ")
   
pt=float(pt)
pt=round(pt)

pi=input("ingrese su nota de interrogaciones: ")

pi=float(pi)
pi=round(pi)
   
ne=input("ingrese nota del examen: ")

ne=float(ne)
ne=round(ne)
pp=input("ingrese su nota de presentacion: ")

pp=float(pp)
pp=round(pp)

resultado=pt*0.3+pi*0.3+0.3*ne+0.1*pp


print("El promedio es",resultado)
