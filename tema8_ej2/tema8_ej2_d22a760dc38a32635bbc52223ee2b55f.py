def buscarTodas(a,b):
  resultado=" "
  indice=0
  while indice != -1:
    if(a.find(b, indice) != -1):
      resultado+=' '+str(a.find(b, indice))
    indice=a.find(b, indice)
    if(indice == 0):
      indice+=1
    else:
        indice+=1

  return resultado


if __name__ == "_main_":
  a = input("Ingresa la palabra o frase que quieras: ")
  a.lower
  b = input("Ingresa la palabra que quieras buscar dentro de la frase: ")
  b.lower
  resultado  = buscarTodas(a,b)
 print("El resultado es : ",resultado)