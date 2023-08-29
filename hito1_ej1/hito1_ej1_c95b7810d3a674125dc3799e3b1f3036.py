#Nota final
# inputs
PT = float(input('inserte promedio de tareas: '))
PI = float(input('inserte promedio de interrogaciones: '))
NE = float(input('inserte nota de examen: '))
PP = float(input('inserte nota de presentacion: '))

# proce
x = 0.3*PT+0.3*PI+0.3*NE+0.1*PP


# output
print("su promedio es: " , round(x, 1))
      