#Nota final
PT = eval(input("ingrese su nota en tareas: "))
PI = eval(input("ingrese su nota en interrogaciones: "))
NE = eval(input("ingrese su nota en examen: "))
PP = eval(input("ingrese su nota de presentacion: "))
Notas = PT+PI+NE
final = (Notas*0.3)+(PP*0.1)
print(round(final,1))