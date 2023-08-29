#Nota final
PT = eval(input("ingrese su nota de tareas:"))
PI = eval(input("ingrese su nota de interrogaciones:"))
NE = eval(input("ingrese su nota de su examen:"))
PP = eval(input("ingrese su nota de presentacion:"))
Notas = PT+PI+NE
Promedio_final = (Notas*0.3) + (PP*0.1)
print(round(Promedio_final,1))      