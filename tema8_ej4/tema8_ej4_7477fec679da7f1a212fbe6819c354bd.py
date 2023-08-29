def rot13(palabra):
    search="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    busquedaRetorno="NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    retorno=""
    for i in range(0,len(palabra)):
        letraBuscada=palabra[i]
        posicionLetra=-1
        for j in range(0,len(search)):
            if letraBuscada==search[j]:
                posicionLetra=j
                break
        if posicionLetra==-1:
            retorno= retorno+letraBuscada
        else:
            retorno=retorno+busquedaRetorno[posicionLetra]
    return retorno
                      