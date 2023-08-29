PT = eval(input("Notas de Tareas: "))
PI = eval(input("Notas de Interrogaciones: "))
NE = eval(input("Notas de Examen: "))
PP = eval(input("Notas de Presentación: "))
print("El promedio final es: ", round((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP), 1))
      