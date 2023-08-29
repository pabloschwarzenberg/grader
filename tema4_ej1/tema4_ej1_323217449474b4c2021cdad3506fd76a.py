def ocultar_letras(palabra,cantidad):
    import random
    palabra=list(palabra)
    for w in range(1,cantidad+1):
        num=random.randint(0,len(palabra)-1)
        palabra[num]="_"
    nueva=""
    for tmp in palabra:
        nueva=nueva+tmp
    return nueva
def revisar_palabra(palabra_secreta,palabra,letra):
    secreta=list(palabra_secreta)
    palabratmp=list(palabra)
    if (letra==palabra_secreta):
        return palabra_secreta
    posiciones=[]
    cont=0
    for tmp in secreta:
        if (letra==tmp):
            posiciones.append(cont)            
        cont=cont+1    
    for posi in posiciones:
        palabratmp[posi]=letra
    resultado=""
    for k in palabratmp:
        resultado=resultado+k
    return resultado

if __name__ == "__main__":
    pass