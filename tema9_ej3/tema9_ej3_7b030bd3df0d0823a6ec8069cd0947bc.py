def decodificar(mensaje):
    global numero
    global resultado_1
    global resultado_2
    global resultado_3
    global resultado_4
    numero = 0
    resultado_1 = 0
    resultado_2 = 0
    resultado_3 = 0
    resultado_4 = 0
    lista = list(mensaje)
    lista2 = []
    lista3 = []
    lista4 = []
    lista5 = []
    for i in range(len(lista)):
        if("0" == lista[i] or "1" == lista[i]):
            lista2.append(lista[i])
        elif("," == lista[i]):
            break
    lista = lista[9:17]
    for j in range(len(lista)):
        if("0" == lista[j] or "1" == lista[j]):
            lista3.append(lista[j])
        elif("," == lista[j]):
            break
    lista = list(mensaje)
    lista = lista[18:26]
    for k in range(len(lista)):
        if("0" == lista[k] or "1" == lista[k]):
            lista4.append(lista[k])
        elif("," == lista[k]):
            break
    lista = list(mensaje)
    lista = lista[27:35]
    for l in range(len(lista)):
        if("0" == lista[l] or "1" == lista[l]):
            lista5.append(lista[l])
        elif("," == lista[l]):
            break
    letra2 = "".join(lista2)
    letra3 = "".join(lista3)
    letra4 = "".join(lista4)
    letra5 = "".join(lista5)

    letra2 = (letra2)[::-1]
    letra3 = (letra3)[::-1]
    letra4 = (letra4)[::-1]
    letra5 = (letra5)[::-1]

    letra2 = list(letra2)
    letra3 = list(letra3)
    letra4 = list(letra4)
    letra5 = list(letra5)

    for i in range(len(letra2)):
        if(True):
            calculo = float(letra2[i]) * 2 **numero
            resultado_1 = resultado_1 + int(calculo)
            numero = numero + 1
    numero = 0
    for i in range(len(letra3)):
        if(True):
            calculo = float(letra3[i]) * 2 **numero
            resultado_2 = resultado_2 + int(calculo)
            numero = numero + 1
    numero = 0
    for i in range(len(letra4)):
        if(True):
            calculo = float(letra4[i]) * 2 **numero
            resultado_3 = resultado_3 + int(calculo)
            numero = numero + 1
    numero = 0
    for i in range(len(letra5)):
        if(True):
            calculo = float(letra5[i]) * 2 **numero
            resultado_4 = resultado_4 + int(calculo)
            numero = numero + 1
    resultado_1 = chr(resultado_1)
    resultado_2 = chr(resultado_2)
    resultado_3 = chr(resultado_3)
    resultado_4 = chr(resultado_4)
    mensaje = resultado_1+resultado_2+resultado_3+resultado_4
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)