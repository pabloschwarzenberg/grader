#Ingresar las 4 notas

PT = float(input("Escriba su nota de tareas:"))
PI = float(input("Escriba su nota de interrogacion:"))
NE = float(input("Escriba su nota de exament:"))
PP = float(input("Escriba su nota de presentacion:"))

#Procedimiento

Promedio = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

#Resultado

print("Su promedio de las cuatro notas es", "{:.1f}".format(Promedio))

