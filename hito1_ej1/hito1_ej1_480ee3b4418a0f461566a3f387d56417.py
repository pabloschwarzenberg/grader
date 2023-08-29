#Nota final
PT=eval(input("ingresar nota de tareas: "))
PI=eval(input("ingresar nota interrogaciones: "))
NE=eval(input("ingresar nota examen: "))
PP=eval(input("ingresar nota presentacion: "))

suma=0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
round(suma,1)
print("el resultado es:",suma)