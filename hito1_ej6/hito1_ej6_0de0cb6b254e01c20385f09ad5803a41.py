numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un segundo numero: "))
numero3 = int(input("Ingrese un tercer numero: "))

numero_menor = min(numero1,numero2,numero3)
numero_mayor = max(numero1,numero2,numero3)
numero_central = (numero1 + numero2 + numero3) - (numero_mayor + numero_menor)

print(str(numero_menor) + "," + str(numero_central) + "," + str(numero_mayor))