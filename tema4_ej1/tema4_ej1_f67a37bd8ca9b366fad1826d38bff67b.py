def ocultar_letras(palabra,cantidad):
    c=0
    while c<cantidad:
        letra=palabra[c]
        rep=palabra.count(letra)
        c=c+rep-1
        palabra=palabra.replace(letra,"_")
        c+=1
    return palabra
def revisar_letra(palabra_secreta, palabra, letra):
    if letra in palabra_secreta:
        largo=len(palabra_secreta)
        pos1=palabra_secreta.index(letra,0,round((largo/2)))
        pos2=palabra_secreta.index(letra,round((largo/2)), largo)
        palabra = palabra[:pos1] + letra + palabra[pos1 + 1:]
        palabra = palabra[:pos2] + letra + palabra[pos2 + 1:]
        return palabra

if __name__ == "__main__":
    pass
         