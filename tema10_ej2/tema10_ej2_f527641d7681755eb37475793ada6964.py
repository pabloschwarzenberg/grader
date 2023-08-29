name =[]
def levenshtein(palabra1,palabra2):
    if palabra1 == palabra2:
        return "0D"
    else:
        p1 = len(palabra1)
        p2 = len(palabra2)
        palabra_larga = palabra2
        palabra_corta = palabra1
        if (p1 > p2):
            palabra_larga = palabra1 
            palabra_corta = palabra2
        for letra in palabra_corta:
            if letra in palabra_larga:
                palabra_larga = palabra_larga.replace(letra,"",1)
        if len(palabra_larga) > 1:
            return "+1"
        else:
            if p1 == p2:
                return "1S"
            else:
                return "IB"

if name=="main":
    pass