#Nota final
PT = eval(input("ingrese su nota de tareas."))
PI = eval(input("ingrese su nota de interrogaciones."))
NE = eval(input("ingrese nota de su examen."))
PP = eval(input("ingrese su nota de presentacion."))
NOTA = PT+PI+NE
promedio_final = (NOTA*0.3)+(PP*0.1)
print(round(promedio_final,1))