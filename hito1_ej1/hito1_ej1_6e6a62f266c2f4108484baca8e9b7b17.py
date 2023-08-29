#Nota final
T=float(input("Ingrese la nota de su tarea: "))
I=float(input("Ingrese la nota de su interrogacion: "))
E=float(input("Ingrese la nota de su examen: "))
P=float(input("Ingrese la nota de su presentacion: "))
ecuacion=0.3*T + 0.3*I + 0.3*E + 0.1*P
redondeado=round(ecuacion, 1)
print("Tu Promedio final es: ", ecuacion)