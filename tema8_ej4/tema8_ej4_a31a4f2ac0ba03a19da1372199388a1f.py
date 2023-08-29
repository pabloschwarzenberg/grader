def rot13(palabra):
    primeras = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    segundas = ["n","o","p","q","r","s","t","u","v","w","x","y","z"]

    largo = len(palabra)
    constante = 0
    nueva = ""
    while constante < largo:
        letra = palabra[constante]
        if letra in primeras:
            que = primeras.index(letra)
            qued = segundas[que]

            nueva = nueva + qued
        elif letra in segundas:
            que = segundas.index(letra)
            qued = primeras[que]

            nueva = nueva + qued
        constante += 1

    return nueva