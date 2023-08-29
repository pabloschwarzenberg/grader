name =[]
def levenshtein(palabra_1,palabra_2):
    if palabra_1 == palabra_2:
        return "0D"
    else:
        P1 = len(palabra_1)
        P2 = len(palabra_2)
        palabra_larga = palabra_2
        palabra_corta = palabra_1
        if (P1 > P2):
            palabra_larga = palabra_1 
            palabra_corta = palabra_2
        for letra in palabra_corta:
            if letra in palabra_larga:
                palabra_larga = palabra_larga.replace(letra,"",1)
        if len(palabra_larga) > 1:
            return "+1"
        else:
            if P1 == P2:
                return "1S"
            else:
                return "IB"