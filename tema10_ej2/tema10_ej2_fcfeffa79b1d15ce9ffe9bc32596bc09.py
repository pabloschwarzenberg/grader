#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):
    lenPalabra1 = len(palabra1)
    lenPalabra2 = len(palabra2)

    listaPalabra1 = []
    for i in range(0, len(palabra1)):
        listaPalabra1.append(palabra1[i])

    listaPalabra2 = []
    for j in range(0, len(palabra2)):
        listaPalabra2.append(palabra2[j])

    lisValores = []
    valor = 0

    if palabra1 == palabra2:
        resultado = "0D"

    if palabra1 != palabra2 and lenPalabra1 == lenPalabra2:
        for i in range(lenPalabra1):
            lisTuplaResultado = []
            if listaPalabra1[i] == listaPalabra2[i]:
                valor = 0
                lisTuplaResultado.append(valor)
                lisTuplaResultado.append(0)
            if listaPalabra1[i] != listaPalabra2[i]:
                valor = 1
                lisTuplaResultado.append(valor)
                lisTuplaResultado.append("S")
            lisValores.append(lisTuplaResultado)

        distancia = 0
        for i in range(0, len(lisValores)):
            distancia = distancia + lisValores[i][0]

        if distancia > 1:
            resultado = "+1"
        if distancia == 1:
            resultado = "1S"

    if lenPalabra1 > lenPalabra2:
        palabraLarga = palabra1
        palabraCorta = palabra2

    else:
        palabraLarga = palabra2
        palabraCorta = palabra1

    lisSuma = []
    if len(palabraLarga) == len(palabraCorta) + 1:
        for i in range(0, len(palabraCorta)):
            if palabraCorta[i] in palabraLarga:
                suma = 0
                lisSuma.append(suma)
            else:
                suma = 1
                lisSuma.append(suma)

            if sum(lisSuma) == 0:
                resultado = ("IB")
            else:
                resultado = ("+1")
    if palabra1 != palabra2 and len(palabraLarga) != len(palabraCorta) + 1 and len(palabraLarga) != len(palabraCorta):

        suma = 0

        lisPalabraLarga = []
        for i in range(0, len(palabraLarga)):
            lisPalabraLarga.append(palabraLarga[i])

        lisPalabraCorta = []
        for j in range(0, len(palabraCorta)):
            lisPalabraCorta.append(palabraCorta[j])

        listaLista = []
        for i in range(0, len(lisPalabraLarga)):
            lisFila = []
            for j in range(0, len(lisPalabraCorta)):
                if lisPalabraLarga[i] == lisPalabraCorta[j]:
                    lisFila.append(0)
                else:
                    lisFila.append(1)
            listaLista.append(lisFila)

        lisResultadosFila = []
        for i in range(0, len(listaLista)):
            lisTuplaResultado = []
            estaRara = 0
            sumaPorFila = 0
            for j in range(0, len(listaLista[i])):
                sumaPorFila = sumaPorFila + listaLista[i][j]
                if j == i and listaLista[i][j] != 0:
                    estaRara = 1
            if sumaPorFila == len(lisPalabraCorta):
                lisTuplaResultado.append(1)
                lisTuplaResultado.append("B")
            if sumaPorFila < len(lisPalabraCorta) and estaRara == 1:
                lisTuplaResultado.append(1)
                lisTuplaResultado.append("S")
            if sumaPorFila < len(lisPalabraCorta) and estaRara == 0:
                lisTuplaResultado.append(0)
                lisTuplaResultado.append(0)
            lisResultadosFila.append(lisTuplaResultado)

        lisResultadosColumna = []
        for i in range(0, len(lisPalabraCorta)):
            lisTuplaResultadoC = []
            estaRara2 = 1
            sumaPorColumna = 0
            for j in range(0, len(listaLista)):
                sumaPorColumna = sumaPorColumna + listaLista[j][i]
                if j == i and listaLista[j][i] == 0:
                    estaRara2 = 0
                if j == len(listaLista) - 1 and i == len(lisPalabraCorta) - 1 and listaLista[j][i] == 0:
                    estaRara2 = 0
            if sumaPorColumna == len(lisPalabraLarga) - 1 and estaRara2 == 0:
                lisTuplaResultadoC.append(0)
                lisTuplaResultadoC.append(0)
            if sumaPorColumna == len(lisPalabraLarga) - 1 and estaRara2 == 1:
                lisTuplaResultadoC.append(1)
                lisTuplaResultadoC.append("S")
            if sumaPorColumna < len(lisPalabraLarga) - 1:
                lisTuplaResultadoC.append(1)
                lisTuplaResultadoC.append("B")
            lisResultadosColumna.append(lisTuplaResultadoC)

        distancia = 0

        for i in range(0, len(lisResultadosFila)):
            distancia = distancia + lisResultadosFila[i][0]

        for j in range(0, len(lisResultadosColumna)):
            distancia = distancia + lisResultadosColumna[j][0]

        if distancia > 1:
            resultado = "+1"

        if distancia == 1:
            for i in range(0, len(lisResultadosFila)):
                if lisResultadosFila[i][1] == "B":
                    resultado = "IB"

    return (resultado)           