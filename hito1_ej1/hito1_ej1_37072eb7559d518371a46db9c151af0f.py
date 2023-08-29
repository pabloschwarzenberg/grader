#Nota final
pt = float(input("ingrese las notas de las tareas: "))
pi = float(input("ingrese las notas de las interrogaciones: "))
ne = float(input("ingrese las notas de los examenes: "))
pp = float(input("ingerse las notas de las presentaciones: "))

#formula 

PF = 0.3 * (pt) + 0.3 * (pi) + 0.3 * (ne) + 0.1 * (pp)

#salida
print("su promedio final es", PF)