#Nota final
##Dar variables a cada datos
PT=float(input("ingrese notas de tareas:"))
PI=float(input("ingrese notas de interrogaciones:"))
NE=float(input("ingrese notas de examen:"))
PP=float(input("ingrese notas de presentacion:"))
#luego usar formula para sacar la nota final que es = ( 0.3PT + 0.3PI + 0.3NE + 0.1PP)

promedio = round((0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP),1)
#Luego imprimimos el resultado
print("su nota final es:  ", promedio)