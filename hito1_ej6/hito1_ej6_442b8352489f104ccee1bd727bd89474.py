def ordenar_numeros(a, b, c):
    numeros = [a, b, c]
    numeros.sort()
    return numeros
    #____________________________________
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
numeros_ordenados = ordenar_numeros(numero1, numero2, numero3)

print("Números ordenados:", ", ".join(str(num) for num in numeros_ordenados))