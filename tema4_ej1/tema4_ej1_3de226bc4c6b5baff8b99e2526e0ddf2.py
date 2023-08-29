import random
def ocultar_letras(palabra,cantidad):
    b=len(palabra)
    i=0
    while i<cantidad:
        a=random.randint(0,b)
        palabra=palabra[0:a]+"_"+palabra[a+1:]
        i=i+1
    return palabra
print(ocultar_letras(palabra, cantidad))
def revisar_letra(palabra_secreta,palabra,letra):
    palabra=palabra.replace("_","letra")
    if palabra==palabra_secreta:
        return palabra

if __name__ == "__main__":
    pass
         