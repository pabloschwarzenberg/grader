PT = float(input("nota de tareas: "))
PI = float(input("nota de interrogaciones: "))
NE = float(input("nota de examenes: "))
PP = float(input("nota de presentación: "))

ptf = PT*0.3
pif = PI*0.3
nef = NE*0.3
ppf = PP*0.1

vf = ptf+pif+nef+ppf

print("el promedio final es: ",round(vf,2))