def rot13(palabra):
    palabra=palabra.lower()
    primeras="abcdefghijklm"
    segundas="nopqrstuvwxyz"
    salida=""
    for letra in palabra:
        if letra in primeras:
            p=primeras.index(letra)
            salida=salida+segundas[p]
        else:
            p=segundas.index(letra)
            salida=salida+primeras[p]    
    return (salida)