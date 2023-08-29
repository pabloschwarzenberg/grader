def buscarTodas (a,b):
  #---Variables-----
  indice_Funcion = ""
  numeros = 0
  #-----------------
  for i in a:
    numeroString = str(numeros)
    if i == b:
      if indice_Funcion == "":
        indice_Funcion += numeroString
      else:
        indice_Funcion += " "
        indice_Funcion += numeroString
    numeros += 1
  return indice_Funcion