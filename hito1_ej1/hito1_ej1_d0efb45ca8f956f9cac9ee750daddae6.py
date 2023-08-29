#Nota final

#Requisitos: PT = Tareas, PI = Interrogaciones, NE = Examen, PP = Presentacion.
#Formula a usar: 0.3PT + 0.3PI + 0.3NE + 0.1PP.

#Entrada
PT = float(input("Ingrese los puntos de tareas: "))
PI = float(input("Ingrese puntos de interrogaciones: "))
NE = float(input("Ingrese puntos de examen: "))
PP = float(input("Ingrese puntos de presentacion: "))

#Procesamiento de datos

promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

promedio = round(promedio, 1)

#Salida

print("El promedio final es: " , promedio)