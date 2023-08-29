#Nota final
pt = float(input("Ingrese sus Notas de Tarea: "))
pi = float(input("Ingrese sus Notas de Interrogaciones: "))
ne = float(input("Ingrese sus Notas de Examen: "))
pp = float(input("Ingrese sus Notas de Presentacion: "))
prf= 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp
print("su promedio final es: ", round(prf, 1))      