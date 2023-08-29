def ordenar_numeros(numero1, numero2, numero3) :
    numeros = [numero1, numero2, numero3]
    numeros.sort()

    print(",".join(str(numeros) for num in numeros))

numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))
numero3 = int(input("ingrese el tercer numero: "))
ordenar_numeros(numero1, numero2, numero3)
