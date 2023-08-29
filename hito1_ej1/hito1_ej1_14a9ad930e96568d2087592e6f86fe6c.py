print("Programa para calcular promedio")
#datos
PT = float(input("Ingresa la nota tarea: "))
PI = float(input("Ingresa la nota de interrogacion: "))
NE = float(input("Ingresa la nota de examen: "))
PP = float(input("Ingresa la nota de tu presentación: "))
#calculos
promedio = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)
p_r = round(promedio , 1)
#resultado
print(p_r)