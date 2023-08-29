def palindromo(palabra):
    listaletras=list(palabra)
    if len(listaletras)<=1:
        return True
    else:
        a=listaletras.pop(0)
        b=listaletras.pop(-1)
        nuevalista=listaletras
        if a==b:
            return palindromo(nuevalista)
        else:
            return False
           