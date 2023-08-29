def decodificar(mensaje):
  lista = mensaje.split(",")
  lista2 = []
  lista3 = []
  for i in range(0,len(lista)):
      decimal = int(lista[i],2)
      lista2.append(decimal)
      print(lista2)
      
  for x in range(0,len(lista2)):
    num = chr(lista2[x])
    lista3.append(num)
  return("".join(lista3))


print(decodificar("01101000,01101111,01101100,01100001"))