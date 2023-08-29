print("¡hola!, calcula tu promedio")

pt=input("ingrese su nota de tareas: ")
pt=float(pt)
pi=input("ingrese su nota de interrogaciones: ")
pi=float(pi)
ne=input("ingrese nota del examen: ")
ne=float(ne)
pp=input("ingrese su nota de presentacion: ")
pp=float(pp)
resultado=pt*0.3+pi*0.3+0.3*ne+0.1*pp
resultado= round(resultado,1)
print("El promedio es",resultado)
