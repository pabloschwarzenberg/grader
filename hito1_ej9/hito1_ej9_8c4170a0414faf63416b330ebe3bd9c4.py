#Sistema de Ecuaciones

#ENTRADA

valor1= int(input("Inserte un valor para 1: "))

valor2 = int(input("Inserte un valor 2: "))

valor3 = float(input("Inserte valor para 3: "))

valor4 = int(input("Inserte valor para 4: "))

valor5 = float(input("Inserte un valor para 5: "))

valor6 = int(input("Inserte un valor para 6: "))

#PROCESAMIENTO

y = (valor1 * valor4 * valor6 - valor3 ) // (valor1 * valor5 - valor4 * valor2)

x = (valor3 * valor5 - valor6 * valor2) // (valor1 * valor4 * valor5 - valor2)

#SALIDA

print("x=" + str(x) + "y=" + str(y))