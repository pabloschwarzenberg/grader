def rot13(palabra):
    busqueda="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    busquedaRetorno="NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    retorno=""
    for i in range(0,len(palabra)):
        letraBuscada=palabra[i]
        posicionLetra=-1
        for j in range(0,len(busqueda)):
            if letraBuscada==busqueda[j]:
                posicionLetra=j
                break
        if posicionLetra==-1:
            retorno= retorno+letraBuscada
        else:
            retorno=retorno+busquedaRetorno[posicionLetra]
    return retorno
           