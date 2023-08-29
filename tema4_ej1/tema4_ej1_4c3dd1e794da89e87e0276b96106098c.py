import random
frase = "berneri amoros gramsci".split()

def ocultar_letras(frase,cantidad):
    frase = list(frase)
    for i in range(cantidad):
        posiciones = random.randint(1,len(frase)) - 1
        if frase[posiciones] == "_":
            posiciones = random.randint(1, len(frase)) - 1
        frase[posiciones] = "_"
    frase = "".join(frase)
    return frase
    
    
def revisar_letra(palabra_secreta,palabra,letra):
    palabra = list(palabra)
    palabra_secreta = list(palabra_secreta)
    contador = 0
    numletra = palabra_secreta.count(letra)
    if numletra > 0:
        for i in palabra_secreta:
            if i == letra:
                palabra_secreta[contador] = contador
            contador += 1
        for p in range(len(palabra)):
            try:
                pos1 = palabra_secreta.index(p)
            except ValueError:
                continue
            pos1 = palabra_secreta.index(p)
            palabra[pos1] = letra
    palabrafinalizada = "".join(palabra)
    return palabrafinalizada    

if __name__ == "__main__":
    pass
         