
def levenshtein(palabra1,palabra2):
    len_palabra1 = len(palabra1)
    len_palabra2 = len(palabra2)
    remplazar = 0
    insertar = 0

    if(len_palabra1 == len_palabra2):
        for index in range(0, len(palabra1)):
            if palabra1[index] != palabra2[index]:
                remplazar += 1
    else:
        dif = len_palabra2 - len_palabra1
        if( dif > 1 or dif < -1):
            return '+1'
        else:
            if(len(palabra1) < len(palabra2)):
                palabra_menor_rango = palabra1
                palabra_mayor_rango = palabra2
            else:
                palabra_menor_rango = palabra2
                palabra_mayor_rango = palabra1
            pl = palabra_menor_rango
            list_palabra_menor_rango = list(palabra_menor_rango)
            for index in range(0, len(list_palabra_menor_rango)):
                if palabra_menor_rango[index] != palabra_mayor_rango[index]:
                    print(index, palabra_mayor_rango[index])
                    list_palabra_menor_rango.insert(index, palabra_mayor_rango[index])
                    print(list_palabra_menor_rango)
                    palabra_menor_rango = "".join(list_palabra_menor_rango)
                    print(palabra_menor_rango)
                    insertar += 1
            print(insertar)
            if insertar > 1:
                return '+1'
            else:
                return 'IB'
    if remplazar == 0:
        return '0D'
    elif remplazar == 1:
        return '1S'
    elif remplazar > 1:
        return '+1'