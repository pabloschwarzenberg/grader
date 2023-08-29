#Ordenar tres números
def ordenar_numeros(a, b, c):
    numeros = [a, b, c]
    numeros.sort()
    numeros_ordenados = ""
    
    for i in range(len(numeros)):
        numeros_ordenados += str(numeros[i])
        if i < len(numeros) - 1:
            numeros_ordenados += ","
    
    print("Números ordenados:", numeros_ordenados)

a = int(input("Ingrese el 1er número: "))
b = int(input("Ingrese el 2do número: "))
c = int(input("Ingrese el 3er número: "))

ordenar_numeros(a, b, c)