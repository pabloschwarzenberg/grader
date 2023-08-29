def levenshtein(palabra1,palabra2):
    sem = 0
    while True:
        if len(palabra1)==len(palabra2):
            ref = palabra2
            for letra in palabra1:
                if letra in palabra2:
                    sem += 1
                    palabra2 = palabra2.replace(letra, "", 1)
            if (len(ref) - sem)==1:
                respuesta="1S"
                break


        if len(palabra1) > len(palabra2): palabra1, palabra2 = palabra2, palabra1
        ref = palabra2
        for letra in palabra1:
            if letra in palabra2:
                sem += 1
                palabra2 = palabra2.replace(letra, "", 1)
        if (len(ref) - sem)>1:
            respuesta="+1"
            break
        if (len(ref) - sem)==1:
            respuesta="IB"
            break
        if (len(ref) - sem)==0:
            respuesta="0D"
            break
    return respuesta



if __name__=="__main__":
    a="gato"
    b="gallina"
    levenshtein(a, b)

    a = "gallina"
    b = "gallina"
    levenshtein(a, b)

    a = "caro"
    b = "cara"
    levenshtein(a, b)

    a = "jaron"
    b = "jarron"
    levenshtein(a, b)

    a = "Limon"
    b = "limon"
    levenshtein(a, b)

    a = "jarron"
    b = "melon"
    levenshtein(a, b)