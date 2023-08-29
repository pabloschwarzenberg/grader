import random
palabras_secreta=["computador","televisor","bicicleta"]
g = random.randint(0,2)
palabra_secreta = palabras_secreta[g]

def ocultar_letras(palabra,cantidad):
    global palabras_secreta
    palabra = list(palabras_secreta)
    i = 0
    while i < cantidad:
        palabra = list(palabra)
        a = random.randint(0,len(palabra)-1)
        palabra[a]= "_"
        palabra = "".join(palabra)
        i = i + 1
    return palabra
    
def revisar_letra(palabra_secreta,palabra,letra):
    if palabra_secreta.find(letra) == -1:
        print("esa letra no esta")
    else:
        slot = 0
        while True:
            slot = palabra_secreta.find(letra,slot)
            if slot == -1:
                break
            palabra = list(palabra)
            palabra[slot] = letra
            palabra = "".join(palabra)
            slot = slot + 1
    return palabra
if __name__ == "__main__":
    pass
         