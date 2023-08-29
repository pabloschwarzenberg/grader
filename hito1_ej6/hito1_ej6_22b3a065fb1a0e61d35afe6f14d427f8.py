numero_uno = int(input("ingrese su primer numero: "))
numero_dos = int(input("ingrese su segundo numero: "))
numero_tres = int(input("ingrese su tercer numero: "))
maximo = max(numero_uno, numero_dos, numero_tres)
minimo = min(numero_uno, numero_dos, numero_tres)
medio = (numero_uno + numero_dos + numero_tres) - maximo - minimo
print("de menor a mayor sus numeros son: ", minimo, ",", medio, ",", maximo)