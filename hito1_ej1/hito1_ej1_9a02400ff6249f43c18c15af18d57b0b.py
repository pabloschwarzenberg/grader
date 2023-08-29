#ingresar notas

PT = float(input("Ingrese nota de las tareas: "))
PI = float(input("Ingrese nota de las interrogaciones: "))
NE = float(input("Ingrese nota del examen: "))
PP = float(input("Ingrese nota de la presentacion: "))

#calcular promedio

PF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

#redondear

PF = round(PF,1)

#imprimir promedio redondeado
print("Su promedio final es: ",PF)
      