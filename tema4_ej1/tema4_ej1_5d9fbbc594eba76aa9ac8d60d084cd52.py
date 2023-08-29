import random
def ocultar_letras(palabra,cantidad):
    posicion = []
    palabraN = []
    con = 0
    palabraF = ""
    for i in palabra:
        palabraN.append(i)
    while con < cantidad:
        a = random.randint(0,(len(palabra)-1))
        if a not in posicion:
            palabraN[a] = "_"
            posicion.append(a)
            con+=1
    for j in palabraN:
        palabraF += j
    return palabraF 

def revisar_letra(palabra_secreta,palabra,letra):
    palabraO = []
    palabraR = []
    palabraKI = ""
    for i in palabra_secreta:
        palabraO.append(i)
    for j in palabra:
        palabraR.append(j)
    for k in range(len(palabraR)):
        if palabraR[k] == "_":
            if palabraO[k] == letra:
                palabraR[k] = letra
    for l in palabraR:
        palabraKI+=l
    return palabraKI

if __name__ == "__main__":
    pass
         