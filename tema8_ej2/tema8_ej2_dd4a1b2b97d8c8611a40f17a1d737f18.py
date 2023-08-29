def buscarTodas(a,b):
    #Dar un texto
    texto_a=""
    i=0
    #Revisa cada palabra y con su ubicación.
    while i<len(a):
        if a[i]==b:
            texto_a=texto_a+str(i)+" "
        i=i+1
    return texto_a.strip()
  