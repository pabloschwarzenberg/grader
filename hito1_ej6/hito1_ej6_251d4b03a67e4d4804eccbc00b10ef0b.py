#Ordenar tres números
numero_uno = int(input("Ingrese un numero:"))

numero_dos = int(input("Ingrese un segundo numero:"))

numero_tres = int(input("Ingrese un tercer numero:"))

numero_max = max(numero_uno,numero_dos,numero_tres)

numero_min = min(numero_uno,numero_dos,numero_tres)

total = (numero_uno + numero_dos + numero_tres) - numero_max - numero_min

print(numero_min ,", ", total ,", ",numero_max)

