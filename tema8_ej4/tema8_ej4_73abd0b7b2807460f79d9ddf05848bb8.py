cadena = int(input("Ingrese cadena a cifrar: "))
cadena_l1 = list(cadena)
cadena_l2 = list(cadena)
indice = 0
for caracter in cadena_l1:
    nAscii = ord(caracter)
    if ((nAscii >= 65 and nAscii <= 77)or(nAscii >= 97 and nAscii <= 109)):
        cadena_l2[indice] = chr(nAscii+13)
    if ((nAscii >= 78 and nAscii <= 90)or(nAscii >= 110 and nAscii <= 122)):
        cadena_l2[indice] = chr(nAscii-13)
    indice += 1
print("cadena original:","".join(cadena_l1))
print("cadena cifrada:","".join(cadena_l2))