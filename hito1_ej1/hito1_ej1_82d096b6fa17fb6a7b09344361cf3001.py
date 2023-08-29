#Programa para calcular el promedio final

PT = float (input("Ingresa tu nota en las tareas: "))
PI = float (input("Ingresa tu nota en las interrogaciones: "))
NE = float (input("Ingresa tu nota en el examen: "))
PP = float (input("Ingresa tu nota en la presentación: "))

profinal = 0.3*(PT) + 0.3*(PI) + 0.3*(NE) + 0.1*(PP)

trueprofinal = round (profinal,1)

print ("Tu promedio final es de " +str(trueprofinal))      