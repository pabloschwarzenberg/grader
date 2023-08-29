#Nota final
PT = float(input("Ingrese nota tareas: "))
PI = float(input("Ingrese nota interrogaciones: "))
NE = float(input("Ingrese nota examen: "))
PP = float(input("Ingrese nota presentación: "))

round(PT)
round(PI)
round(NE)
round(PP)

a= 0.3 * PT 
b= 0.3 * PI
c= 0.3 * NE
d= 0.1 * PP

print(a+b+c+d)