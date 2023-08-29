def jerigonzo(string):
    frase = string
    string_1 = frase.lower()
    vocales = ["a","e","i","o","u","á","é","í","ó","ú"]
    abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    asd = ["p"]
    espacio = [" "]
    texto_listo = []
    for i in string_1:
        if i in abecedario:
            texto_listo.append(i)
        if i in vocales:
            texto_listo.append("p" + i)
        if i in espacio:
            texto_listo.append(" ")
    texto_listo_1 = "".join(texto_listo)
    return texto_listo_1
