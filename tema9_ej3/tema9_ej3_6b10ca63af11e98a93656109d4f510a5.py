def decodificar(mensaje):

  mensaje1 = mensaje.split(",")
  palabra =[]
  for x in range(len(mensaje1)):
    letras = chr(int(mensaje1[x],2))
    palabra.append(letras)
  mensaje = str(palabra[0]) + str(palabra[1]) + str(palabra[2]) + str(palabra[3])

  return mensaje
         