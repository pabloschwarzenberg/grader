#Ordenar tres números
print("ingrese tres numeros enteros: ")

numero_1=eval(input("Ingrese numero uno: "))
numero_2=eval(input("Ingrese numero dos: "))
numero_3=eval(input("Ingrese numero tres: "))

numeros = (numero_1,numero_2,numero_3)

numeros =sorted(numeros)

print ("el orden de los numeros es: ",numeros)      