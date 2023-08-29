#Nota final
# Notas tareas
PT = input("Ingrese notas de tareas: ")
PI = input("Ingrese notas de Interrogaciones: ")
NE = input("Ingrese nota de examen: ")
PP = input("Ingrese notas de presentacion: ")

try:
    PT = float(PT)
    PI = float(PI)
    NE = float(NE)
    PP = float(PP)

    Promedio_final = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)

    round(Promedio_final, 1)
    print("Tu promedio final es: ", Promedio_final)
except ValueError:
    print("Eso no es un numero.") 