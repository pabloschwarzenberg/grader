def ocultar_letras(palabra,cantidad):
    import random
    palabra = list(palabra)
    while cantidad > 0 :
        i = random.randint(0,len(palabra))
        if palabra[i] != "_" :
            palabra[i] = "_"
        else :
            cantidad += 1
        cantidad -= 1
    return ''.join(palabra)

def revisar_letra(palabra_secreta,palabra = "",letra = ""):
    ocultar_letras(palabra)
    palabra_secreta = list(palabra_secreta)
    if palabra == "" and letra != "" :
        for j in range(len(palabra_secreta)) :
            if letra in p == True :
                palabra_secreta[j] = letra
                return ''.join(palabra_secreta)
    if palabra != "" and letra == "" :
        if palabra == p :
            return palabra
         