def levenshtein(palabra1,palabra2):
    if palabra1 == palabra2:
        return "0D"
    else:
        contar          = 0
        largo1          = len(palabra1)
        largo2          = len(palabra2)
        diferencia      = abs(largo1 - largo2)
        palabra_larga   = palabra1
        palabra_corta   = palabra2
        contar2         = 0
        if largo2 > largo1:
            palabra_larga = palabra2
            palabra_corta = palabra1

        for i in range(len(palabra_corta)):
            if palabra1[i]==palabra2[i]:
                contar +=1

        for i in palabra1:
            if i in palabra2:
                contar2 +=1

        if diferencia > 1:
            return "+1"
        elif diferencia == 0 and contar2 == len(palabra1) - 1:
            return "1S"
        elif diferencia >= 1 and contar2 == len(palabra1):
            return "IB"
        elif diferencia + (len(palabra_larga) - contar) + (len(palabra_larga) - contar2) >=2:
            return "+1"