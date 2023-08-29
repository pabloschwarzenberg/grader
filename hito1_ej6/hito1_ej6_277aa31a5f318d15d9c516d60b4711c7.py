numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

numeros_ordenados = sorted([numero1, numero2, numero3])

print("Los numeros ordenados de menor a mayor son: {}, {}, {}".format(*numeros_ordenados))
