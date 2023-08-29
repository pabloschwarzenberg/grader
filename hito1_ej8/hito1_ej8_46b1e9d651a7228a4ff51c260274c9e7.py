#Descomponer un número
 def descomponer_numero(numero):
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = (numero // 1000) % 10

    descomposicion = f"{miles}M + {centenas}C + {decenas}D + {unidades}U"

    return descomposicion


# Pedir al usuario que ingrese un número de hasta 4 dígitos
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Llamar a la función para obtener la descomposición
descomposicion = descomponer_numero(numero)
# Imprimir el resultado
print(descomposicion)
     