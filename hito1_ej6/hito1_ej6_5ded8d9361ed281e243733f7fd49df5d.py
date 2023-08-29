numero_uno = int(input("ingrese el primer número entero: "))
numero_dos = int(input("ingrese el segundo número entero: "))
numero_tres = int(input("ingrese el tercer número entero: "))
numeros = [numero_uno , numero_dos , numero_tres]
numeros.sort()
primero = numeros[0]
segundo = numeros[1]
tercero = numeros[2]
print ("{},{},{}".format(primero, segundo, tercero))