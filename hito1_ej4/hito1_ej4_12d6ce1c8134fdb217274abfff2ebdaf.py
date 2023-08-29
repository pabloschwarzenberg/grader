def cambio_hexa(decimal):
conversion = ""
while decimal // 16 != 0:
resto = str(decimal % 16)
if int(resto) > 9:
lista = (A,B,C,D,E,F)
resto = lista[int(resto)-10]
conversion = resto + conversion
decimal = decimal // 16
return str(decimal) + conversion

numero = int(input("Introduce el numero a cambiar a hexadecimal: "))
print(cambio_hexa(numero))