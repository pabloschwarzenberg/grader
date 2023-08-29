#DATOS
nota1 = eval(input("Ingresa nota tarea: "))
nota2 = eval(input("Ingresa nota interrogaciones: "))
nota3 = eval(input("Ingresa nota Examen: "))
nota4 = eval(input("Ingresa nota Presentacion: "))
# Salida de datos
promedio = (nota1*0.3 + nota2*0.3 + nota3*0.3 + nota4*0.1)

print("El promedio es: ", round(promedio, 1))      