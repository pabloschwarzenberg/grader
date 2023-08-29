def desconro(nro):
    unidades = nro % 10
    decenas = (nro // 10) % 10
    centenas = (nro // 100) % 10
    miles = (nro // 1000) % 10
    
    desco = ""
    if miles >= 0:
        desco += str(miles) + "M + "
    if centenas >= 0:
        desco+= str(centenas) + "C + "
    if decenas >= 0:
        desco+= str(decenas) + "D + "
    if unidades >= 0:
        desco += str(unidades) + "U"
    
    return desco


nro = int(input("Ingrese un número de hasta 4 dígitos: "))

desco= desconro(nro)

print("Resultado:", desco)
