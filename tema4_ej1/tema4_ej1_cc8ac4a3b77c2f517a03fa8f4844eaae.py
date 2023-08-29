from random import randint,choice
def ocultar_letras(palabra,cantidad):
    lp = list(palabra)
    for i in range(cantidad):
        pos=randint(0,len(lp)-1)
        lp[pos]='_'
    return ''.join(lp)
def revisar_letra(palabra_secreta,palabra,letra):
    lp=list(palabra)
    for i in range(len(lp)):
        if lp[i]=='_' and palabra_secreta[i]==letra:
            lp[i]=letra             
    return ''.join(lp)
if __name__=='__main__':
    lista_palabras=['paralelepipedo','tiranosaurio','inspirar','digito','uno','destruccion','etcetera']
    palabra_secreta=choice(lista_palabras)
    cantidad=randint(1,len(palabra_secreta)-1)
    contador=0
    continuar=True
    palabra=ocultar_letras(palabra_secreta,cantidad)
    print('Adivina la palabra\nTienes 7 intentos\nA continuacion, ingresa una letra o arriesgate con la palabra que crees es la correcta')
    while continuar:
        if contador==7:
            print('Perdiste')
            continuar=False
        else:
            print('Palabra:',palabra)
            respuesta=input('Su respuesta: ')
            if respuesta==palabra_secreta:
                continuar=False
                print('Ganaste')
            elif len(respuesta)==1:
                palabra=revisar_letra(palabra_secreta,palabra,respuesta)
                if palabra==palabra_secreta:
                    continuar=False
                    print('Ganaste')
        contador+=1
    print('Palabra secreta:',palabra_secreta)