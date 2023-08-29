#Nota final

#ENTRADA
PT = float(input("ingrese la nota de tareas: "))
PI = float(input("ingrese la nota de interrogaciones: "))
NE = float(input("ingrese la nota del examen: "))
PP = float(input("ingrese la nota de presentacion: "))

#PROCESO
#se guarda el resultado como string para facilitar el siguiente paso
promedio_final = str(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
#i sera la posicion hasta la que se imprimira el resultado (1 decimal, un numero despues del punto) 
i = promedio_final.find(".")+2
#si el segundo decimal es mayor o igual a cinco 
if(int(promedio_final[i]) >= 5):
    #se redondea la primera decena al siguiente numero
    promedio_final = str(float(promedio_final) + 0.1)

#SALIDA
print("el promedio final calculado es: " + promedio_final[ :i])