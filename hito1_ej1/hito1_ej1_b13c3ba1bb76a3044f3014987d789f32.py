#Nota final
PT = eval(input("ingrese su nota de tareas: "))
PI = eval(input("ingrese su nota de interrogaciones: "))
NE = eval(input("ingrese su nota de examen: "))
PP = eval(input("ingrese su nota de presentacion: "))

notas = PT + PI + NE
promedio_final = (notas * 0.3) + (PP * 0.1)

print(round(promedio_final,1))