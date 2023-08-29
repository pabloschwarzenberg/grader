def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()  
    print(f"{numeros[0]}, {numeros[1]}, {numeros[2]}")

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

ordenar_numeros(numero1, numero2, numero3)