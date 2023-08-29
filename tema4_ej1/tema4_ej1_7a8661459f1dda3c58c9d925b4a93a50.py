def ocultar_letras(palabra,cantidad):
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    return palabra

if __name__ == "__main__":
    pass
import math
import random
def ocultar_letras(palabra,cantidad):
    print(cantidad)
    while palabra.count('_') != cantidad:
        print(palabra.count('_'))
        print(palabra)
        pos = random.randint(0,len(palabra)-1)
        print(pos)
        palabra = palabra.replace(palabra[pos],'_',pos)
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    palabra = list(palabra)
    for i in range(0,len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra[i] = palabra_secreta[i]
    palabra = "".join(palabra)
    return palabra

palabras = ["jugar","correr","caminar","fiesta","sorteo","amanecer","programar","java"]

n = random.randint(0,len(palabras)-1)

if __name__ == "__main__":
    cantidad = random.randint(2,len(palabras[n])-1)
    palabra = ocultar_letras(palabras[n],cantidad)
    salir = 1
    while salir != 0:
        
        print('Palabra a adivinar: '+palabra)
        letra = input('Introduzca una letra o una palabra: ')

        if len(letra) == 1:
            palabra = revisar_letra(palabras[n],palabra,letra)
            if  palabra == palabras[n]:
                print('Ganaste!!')
                print('La palabra era: '+palabra)
                salir = 0
            
        else:
            if letra == palabras[n]:
                print('Ganaste!!')
                print('La palabra era: '+palabra)
            else:
                print('Perdio||')
                print('La palabra era: '+palabras[n])
                salir = 0
         