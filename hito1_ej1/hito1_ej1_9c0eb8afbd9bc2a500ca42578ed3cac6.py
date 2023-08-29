#Nota final
print("nota tareas:")
PT = float(input())
print("nota interrogaciones:")
PI = float(input())
print("nota examen:")
NE = float(input())
print("nota presentacion:")
PP = float(input())

SUMA = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)

print("el promedio final es:",round(SUMA,1))