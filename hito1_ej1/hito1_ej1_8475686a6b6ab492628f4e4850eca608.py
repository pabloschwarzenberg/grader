#Nota final
PT = float(input("Ingresa la nota que tuviste en las 'tareas': ")) #EJEMPLO: NOTA PT = 60
PI = float(input("Ingresa la nota que tuviste en las 'Interrogaciones': "))
NE = float(input("Ingresa la nota que tuviste en el 'examen': "))
PP = float(input("Ingresa la nota que tuviste en la 'Presentacion': "))

PromedioFinal = (0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
print('Tu Promedio Final es: ',round(PromedioFinal)