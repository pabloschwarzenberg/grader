def levenshtein(palabra1, palabra2):
    abc = "abcdefghijklmnñopqrstuvwxyz"
    abc += abc.upper()
    cambios = 0
    palabra1 = list(palabra1)
    palabra2 = list(palabra2)
    corta, larga = "", ""
    # Si son iguales
    if palabra1 == palabra2:
        return "0D"
    # Vereficando cantidad de cambios necesarios
    if abs(len(palabra1) - len(palabra2)) >= 2:
        return "+1"
    elif abs(len(palabra1) - len(palabra2)) >= 0:
        # Cuando resta es == 1, seleccion palabra + larga
        if len(palabra1) > len(palabra2):
            larga = palabra1
            corta = palabra2
        elif len(palabra1) < len(palabra2):
            larga = palabra2
            corta = palabra1
        # Comprobando si sacando de la más larga, se iguala a la más corta
        for i in range(len(larga)):
            prueba = larga.copy()
            prueba.pop(i)
            if prueba == corta:
                return "IB"
        if abs(len(palabra1) - len(palabra2)) == 1:
            return "+1"
        # Cuando la resta es == 0
        for i in range(len(palabra1)):
            prueba1 = palabra1.copy()
            prueba2 = palabra2.copy()
            print(prueba1, prueba2)
            for cambio in range(len(abc)):
                print(prueba1, prueba2)
                prueba1[i] = abc[cambio]
                prueba2[i] = abc[cambio]
                if prueba1 == palabra2:
                    return "1S"
                elif prueba2 == palabra1:
                    return "1S"
        return "+1"