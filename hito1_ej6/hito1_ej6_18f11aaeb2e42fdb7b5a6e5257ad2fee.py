def ordenar_numeros(a, b, c):
    numeros = [a, b, c]
    numeros.sort()
    numeros_or = ", ".join(map(str, numeros))
    return numeros_or
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))
final = ordenar_numeros(numero1, numero2, numero3)
print("N° ordenados de menor a mayor:", final)
      