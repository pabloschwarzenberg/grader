#Descomponer un número
   numero = input("Ingrese un número de hasta 4 dígitos: ")
while len(numero) > 4:
    numero = input("El número debe tener máximo 4 dígitos. Ingrese otro número: ")

unidades = int(numero[-1])
decenas = int(numero[-2]) if len(numero) >= 2 else 0
centenas = int(numero[-3]) if len(numero) >= 3 else 0
miles = int(numero[-4]) if len(numero) == 4 else 0

print(f"{miles}M + {centenas}C + {decenas}D + {unidades}U")   