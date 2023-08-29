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

    
if __name__ == "__main__":

    lista_palabras = ['hipopotamo','residuo','eudaimonia','retencion','venecia','tarantula']
    posicion = random.randint(0,len(lista_palabras)-1)
    palabra = lista_palabras[posicion]
    cantidad = random.randint(1,len(palabra))
   
    palabra_ing = ocultar_letras(palabra,cantidad)
    print(palabra_ing)
    cont = 7
    while cont != 0:
        letra = input('Ingrese una letra o arriesgate a la palabra completa: ')
        if palabra == letra:
            break
        elif len(letra) != 1:
            if palabra != letra:
                cont -= 1
                continue
            
        palabra_ing=revisar_letra(palabra,palabra_ing,letra)
        print(palabra_ing)