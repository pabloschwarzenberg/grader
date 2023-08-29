from random import*
def ocultar_letras(palabra,cantidad):
    for x in range(cantidad):
        indice = randint(0,len(palabra)-1)
        print(indice)
        palabra = palabra.replace(palabra[indice],"")
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    if letra in palabra_secreta and letra not in palabra:
        indice = palabra_secreta.find(letra)
        palabra = palabra.replace(palabra[indice],letra)
        return palabra

if __name__ == "__main__":
    pass