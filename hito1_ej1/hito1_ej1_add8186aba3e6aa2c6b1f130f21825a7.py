#Nota final
PT = float(input("Nota de tareas: "))
PI = float(input("Nota de interrogaciones: "))
NE = float(input("Nota de examen: "))
PP = float(input("Nota de pesentación: "))

a = PT*0.3
b = PI*0.3
c = NE*0.3
d = PP*0.1

promedioFinal = a+b+c+d
print(round(promedioFinal, 1))  