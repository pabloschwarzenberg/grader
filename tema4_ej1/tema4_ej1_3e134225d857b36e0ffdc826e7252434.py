import random
from re import X
import string
from tokenize import String

def ocultar_letras(palabra,cantidad):

    z = 0
    x = 0

    if x<cantidad:

        letras = ['a','c','d','e','g','h','i','j','l','m','n','o','p','r']
        letra = random.choice(letras)
        print(letra)
        
        if letra in palabra:
            
            if z < cantidad:
                palabra = palabra.replace(letra, "_") 
                z+=1    
                x+=1
        if z>=cantidad:
            return palabra
##################################################################################################
def revisar_letra(palabra_secreta,palabra,letra):

    tuletra= ''
    maximo_intentos = 0
    if maximo_intentos < 7:

        fallas = 0

        for z in palabra_secreta:
            if z in tuletra:
                 print(z,end="")
            else:
                print(palabra,end="")
                fallas+=1
            
        if fallas == 0:
            break

        tuletra+=letra

    if letra not in palabra_secreta:
        maximo_intentos-=1
    if maximo_intentos == 0:
        print("perdiste")
        
    return palabra

palabras = ['hola','caramelo','caminar','jugar','departamento']
palabra_aleatoria = random.choice(palabras)
cantidad = [1,2,3]
cantidad_letras = random.choice(cantidad)

if __name__ == "__main__":
    pass
         