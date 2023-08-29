def ordenadornumeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros_orden = sorted(numeros)
    resultado = ",".join(str(num) for num in numeros_orden)
    return resultado

numero1 = int(input("introduce el primer numero: "))
numero2 = int(input("introduce el segundo numero: "))
numero3 = int(input("introduce el tercer numero: "))

resultado = ordenadornumeros(numero1, numero2, numero3)
print("numeros ordenados de menos a mas:", resultado)
