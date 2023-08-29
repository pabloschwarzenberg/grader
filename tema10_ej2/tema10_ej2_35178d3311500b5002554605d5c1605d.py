#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    listapalabra_1 = []
    for i in palabra1:
      listapalabra_1.append(i)
    listapalabra_2 = []
    for j in palabra2:
      listapalabra_2.append(j)
    distancia = 0 
    if len(listapalabra_1) == len(listapalabra_2):
      iguales = True
      k = 0
      while k < len(listapalabra_1):
        if listapalabra_1[k] != listapalabra_2[k]:
          iguales = False
        k += 1
      if iguales:
        return "0D"
      elif not iguales:
        for l in range(0,len(listapalabra_1)):
          if listapalabra_1[l] != listapalabra_2[l]:
            distancia += 1
        if distancia == 1:
          return "1S"
        elif distancia > 1:
          return "+1"
    elif len(listapalabra_1) != len(listapalabra_2):
      mayor = max(len(listapalabra_1),len(listapalabra_2))
      menor = min(len(listapalabra_1),len(listapalabra_2))
      cantidad = mayor - menor
      largo = mayor - cantidad
      a = 0
      distancia2 = -1
      while a < largo:
        if listapalabra_1[a] != listapalabra_2[a]:
          distancia2 += 1
        a += 1
      if cantidad == 1 and distancia2 == 1:
        return "IB"
      else:
        return "+1"