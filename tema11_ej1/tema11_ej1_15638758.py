def palindromo(frase):
    lista=list(frase)
    lista1=list(frase)
    lista1.reverse()
    for i in lista1:
        if i==" ":
            lista1.remove(i)
    c="".join(lista1)
    for i in lista:
        if i==" ":
            lista.remove(i)
    d="".join(lista)
    
    if c==d:
        return True
    else:
        return False


           