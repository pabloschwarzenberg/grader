def buscarTodas(a,b):
  lista = list(a)
  listb = []
  for i in range(len(lista)):
    if b == lista[i]:
      a = str(i)
      listb.append(a)
  cadena = " ".join(listb)
  return cadena
           