numeros = []
for i in range(3):
    numero = int(input("Ingrese un numero entero: "))
    numeros.append(numero)
    
numeros.sort()


print(f"{numeros[0]}, {numeros[1]}, {numeros[2]}")