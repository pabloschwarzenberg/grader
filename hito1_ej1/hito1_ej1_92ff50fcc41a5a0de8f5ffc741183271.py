PT = float(input("Nota de tareas: "))
PI = float(input("Nota de interrogaciones: "))
NE = float(input("Nota de examenes: "))
PP = float(input("Nota de presentacion: "))

ptf = 0.3*PT
pif = 0.3*PI
nef = 0.3*NE
ppf = 0.1*PP

vf = ptf+pif+nef+ppf

print("el promedio es:",round(vf,2))