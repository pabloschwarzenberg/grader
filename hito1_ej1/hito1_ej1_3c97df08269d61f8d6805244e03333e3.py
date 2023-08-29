#Nota final
#ENTRADA

#PT = Tareas 
#PI = Interrogaciones
#NE = Examen
#PP = Presentacion 

#aqui al usuario le pedira ingresar sus cuatro notas para sacar promedio
PT = float(input("Ingrese su nota final de sus tareas: "))
PI = float(input("Ingrese su nota final de sus Interrogaciones: "))
NE = float(input("Ingrese su nota final de su Examen: "))
PP = float(input("Ingrese la nota final de su Presentacion: "))

#PROCESAMIENTO

#aqui se calculara su promedio final
Promedio_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

#SALIDA
#imprime su promedio final

print("Su promedio final es: ", round(Promedio_final,1))      