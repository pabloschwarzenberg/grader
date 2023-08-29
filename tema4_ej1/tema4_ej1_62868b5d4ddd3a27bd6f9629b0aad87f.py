def ocultar_letras(palabra,cantidad):
    import random
    for i in range(cantidad):
        q=random.randrange(len(palabra))
        palabra=palabra.replace(palabra[q],"_")
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    contar=palabra_secreta.count(letra)
    n=palabra_secreta.find(letra)
    listapalabra=list(palabra)
    if contar>1 and n!=-1:
      n2=palabra_secreta[n+1:].find(letra)
      listapalabra[n+1+n2]=letra
      palabra="".join(listapalabra)
    if n!=-1 and contar==1:
        listapalabra[n]=letra
        palabra="".join(listapalabra)
    return palabra

