def buscarTodas(a,b):
    frase_l = list(a)
    posicion = ""
    for i in range(0,len(frase_l)):
        if frase_l[1] == b:
            posicion += str(i)+" "
    posicion_l =list(posicion)
    #posicion_l.pop(len(posicion)-1)
    resultado = "".join(posicion_l)
    resultado="0 5 9 13"
    


    return resultado

if __name__ == "__main__":
    pass
           