a = float(input("Ingresa Nota Tareas: "))
b = float(input("Ingresa Nota Interrogaciones: "))
c = float(input("Ingresa Nota Examen: "))
d = float(input("Ingresa Promedio Presentación: "))
suma = float((a*0.3) + (b*0.3) + (c*0.3) + (d*0.10))

print("Nota Presentación: ","{:.1f}".format(suma))     