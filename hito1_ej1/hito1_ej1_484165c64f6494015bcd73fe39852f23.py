#Nota final
print("Ingrese las notas de las pruebas y actividades rendidas:")
n_tar = float(input("Nota Tareas --> "))
n_in = float(input("Nota Interrogaciones --> "))
n_ex = float(input("Nota exámen --> "))
pp = float(input("Presentación --> "))
promedio = (n_tar * 0.3) + (n_in * 0.3) + (n_ex * 0.3) + (pp * 0.1)
print("Su promedio final es de: ", round(promedio, 2))      