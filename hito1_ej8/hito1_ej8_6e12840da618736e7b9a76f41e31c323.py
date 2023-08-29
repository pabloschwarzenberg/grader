def descomponer_numero(numero):
    if len(numero) == 1:
        return f"{numero}U"
    elif len(numero) == 2:
        return f"{numero[0]}D + {numero[1]}U"
    elif len(numero) == 3:
        return f"{numero[0]}C + {numero[1]}D + {numero[2]}U"
    elif len(numero) == 4:
        return f"{numero[0]}M + {numero[1]}C + {numero[2]}D + {numero[3]}U"
    else:
        return "Número inválido"

numero = input("Ingrese un número de hasta 4 dígitos: ")
resultado = descomponer_numero(numero)
print(resultado)
