PT = float(input("Ingresa la PT: "))
PI = float(input("Ingresa la PI: "))
NE = float(input("Ingresa la nota de examen: "))
PP = float(input("Ingresa la nota de presentacion: "))
notaFinal = round(0.3*PT+0.3*PI+0.3*NE+0.1*PP, 1)
print("Tu nota final es: ", notaFinal)
