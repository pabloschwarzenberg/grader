#Nota final
PT = float(input("escriba la nota que tivo en sus tareas: "))
PI = float(input("escriba la nota que tuvo en Interrogaciones: "))
NE = float(input("escriba la nota que tuvo en el Examen: "))
PP = float(input("escriba la nota que tuvo en la Presentacion: "))
promedio_final = ((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP))
print("el promedio final es: ", {round(promedio_final,1)})