#ENTRADA
print("Promedio Notas")

#DESARROLLO
PT = float(input("ingrese nota tareas:"))
PI = float(input("ingrese nota interrogaciones:"))
NE= float(input("ingrese nota examen:"))
PP = float(input("ingrese nota presentacion:"))
suma =0.3*PT+0.3*PI+0.3*NE+0.1*PP

#SALIDA
print("el promedio final es:",round(suma,1))