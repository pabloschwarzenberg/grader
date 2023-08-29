# ingrese las notas
a = eval(input("Ingrese la nota de sus tareas: "))
b = eval(input("Ingrese la nota de sus interrogaciones:  "))
c = eval(input("Ingrese la nota de sus exámenes: "))
d = eval(input("Ingrese la nota de sus exámenes: "))

# cálculo promedio

promedio = ((a * 0.3)+(b * 0.3)+(c * 0.3)+(d * 0.1))

print("Su promedio de notas es ", round(promedio, 1))
