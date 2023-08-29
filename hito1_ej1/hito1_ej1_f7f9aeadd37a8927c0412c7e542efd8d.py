#Nota Final
PT = eval(input("ingrese su nota de tareas:"))
PI = eval(input("ingrese su nota de interrogaciones:"))
NE = eval(input("ingrese su nota de su examen:"))
PP = eval(input("ingrese su nota de presentacion:"))
NOTAS = PT+PI+NE
promedio_final = (NOTAS*0.3) + (PP*0.1)
print(round(promedio_final,1))