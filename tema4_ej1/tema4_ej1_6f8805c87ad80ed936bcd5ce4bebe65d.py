def ocultar_letras(palabra,cantidad):
    ocult=0
    z=0
    while z!=cantidad:
        x= palabra.replace(random.choice(palabra),"_")
        z=x.count("_")
        palabra=x
        ocult+=1
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    palabra_secreta=palabra
    
    return palabra

import random
palabras=["arbol", "helicoptero", "casa", "lechuga", "computador", "juego", "bordar", "barco", "zanahoria"]
palabra= str(random.choice(palabras))
cantidad= random.randint(1,len(palabra))
ocultar_letras(palabra,cantidad)
print(ocultar_letras(palabra,cantidad))

if __name__ == "__main__":
    letra= str(input("Letra que crees es: "))
    revisar_letra(palabra_secreta,palabra,letra)