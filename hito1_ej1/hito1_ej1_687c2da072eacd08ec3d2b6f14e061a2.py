PT = eval(input("ingresa nota de Tareas: "))
PI = eval(input("ingresa nota de Interrogaciones: "))
NE = eval(input("ingresa nota de Examen: "))
PP = eval(input("ingresa nota de Presentacion: "))

suma = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
print("tu promedio es de : ",round(suma,1))
