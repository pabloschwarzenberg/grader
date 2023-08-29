def buscarTodas(a,b):
    lista_a = []
    for i in a:
      lista_a.append(i)
    b =  "t"
    lista = []
    i = 0
    loop = 0
    print(lista_a)
    while i < len(lista_a):
      if lista_a[i] == b:
        numero = lista_a.index(b) + loop
        loop += 1
        lista.append(str(numero))
        lista.append(" ")
        lista_a.remove(b)
      i += 1
    largo = len(lista) - 1
    lista.pop(largo)
    oculto = "".join(lista)
    return oculto 

           