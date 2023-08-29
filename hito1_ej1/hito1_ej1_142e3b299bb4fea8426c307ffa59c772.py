#Nota final
NT=float(input("ingrese su nota de tareas: "))
NI= float(input("ingrese su nota de interrogaciones: "))
NE=float(input("ingrese sus notas de los examenes: "))
NP=float(input("Ingrese notas de presentacion: "))

NF= (0.3*NT + 0.3*NI + 0.3*NE + 0.1*NP)
print("el promedio final del alumno es: " , round(NF,2))     