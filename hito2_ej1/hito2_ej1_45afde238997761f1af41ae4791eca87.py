def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""
    diferencia = len(secuencia1) - len(secuencia2)

    if diferencia > 0:
        secuencia2 = "_" * diferencia + secuencia2
    else:
        secuencia1 = "_" * abs(diferencia) + secuencia1

    for base1, base2 in zip(secuencia1, secuencia2):
        if base1 != base2:
            alineacion += "_"
        else:
            alineacion += base2

    return alineacion

# Obtener las secuencias desde la entrada del usuario
secuencia1 = input().strip()
secuencia2 = input().strip()

# Realizar el alineamiento
alineacion = alinear_secuencias(secuencia1, secuencia2)

# Imprimir el resultado del alineamiento
print([alineacion])
