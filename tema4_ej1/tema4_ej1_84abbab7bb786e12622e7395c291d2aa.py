#Adivina la palabra
from random import randint
def ocultar_letras(palabra,cantidad):
    numero_de_letras=len(palabra)
    palabra=list(palabra)
    
    i=0
    while i<cantidad:
        letra_cambiada=randint(0,numero_de_letras-1)
        if palabra[letra_cambiada]!='_':
            palabra[letra_cambiada]='_'
            i=i+1
    palabra=''.join(palabra)
        
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    numero_de_letras=len(palabra_secreta)
    if letra==palabra_secreta:
        palabra=palabra_secreta

    for i in range(0,numero_de_letras):
        if letra==palabra_secreta[i] and palabra[i]=='_':
            palabra=list(palabra)
            palabra[i]=letra
            palabra=''.join(palabra)
    return palabra

if __name__ == "__main__":
    palabras_secretas=['termometro','perro','doctor','endocrinologo','billetera','segmento','carretera','servicio','policia','adhesivo','gaggero']
    palabra=palabras_secretas[randint(0,len(palabras_secretas)-1)]
    palabra_secreta=palabra
    numero_de_letras=len(palabra)
    cantidad=randint(1,numero_de_letras-2)
    palabra=ocultar_letras(palabra,cantidad)
    for intentos in range(0,8):
        if intentos==7:
                print('Perdiste')
                break
        print('')
        letra=input('Ingrese la letra o palabra que desea probar: ')
        revisar_letra(palabra_secreta,palabra,letra)
         