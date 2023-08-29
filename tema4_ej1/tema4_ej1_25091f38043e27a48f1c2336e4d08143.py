import random
 
def ocultar_letras(palabra,cantidad):

    lista_letras = list(palabra)
    posiciones=[]
    p = 0
    while True:
        a=random.randint(0,len(palabra)-1)
        if len(posiciones)==cantidad:
            break
        if a in posiciones:
            continue
        else:
            posiciones.append(a)
        
    #print(cantidad,posiciones)
    #cantidad es igual al len de posiciones
    for x in range(len(posiciones)):
        lista_letras[posiciones[x]]='_'

        
    palabra = ''.join(lista_letras)
    return palabra
        
def revisar_letra(palabra_secreta,palabra,letra):
    global cont
    if len(letra) == 1:
        if letra in palabra_secreta:
            lista = []
            for i in range(len(palabra_secreta)):
                if letra == palabra_secreta[i]:
                    lista.append(i)
            lista_letras1 = list(palabra)
            a = 0
            for i in range(len(lista)):
                if lista_letras1[lista[i]] =='_':
                    lista_letras1[lista[i]] = letra
                    a += 1
            if a == 0 :
                cont -= 1
    if letra not in palabra_secreta:
        cont -= 1
        return palabra

    palabra = ''.join(lista_letras1)
    return palabra
