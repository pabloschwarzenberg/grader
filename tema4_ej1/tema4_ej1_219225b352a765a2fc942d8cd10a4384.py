def ocultar_letras(palabra,cantidad):
    import random
    i=0
    oculto=[]
    while i < cantidad:
        rand=random.randint(0, len(palabra)-1)
        if not rand in oculto:
            oculto.append(rand)
            i+=1
    copy=""
    letra=0
    while letra < len(palabra):
        if letra in oculto:
            copy += "_"
        else:
            copy += palabra[letra]
        letra+=1
    palabra=copy
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    copy=""
    i=0
    while i < len(palabra_secreta):
        if letra == palabra_secreta[i]:
            copy += letra
        else:
            copy += palabra[i]
        i+=1
    palabra = copy
    return palabra

if __name__ == "__main__":
    pass
         