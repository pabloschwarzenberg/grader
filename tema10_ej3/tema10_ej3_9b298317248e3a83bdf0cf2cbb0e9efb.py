def EncontrarPalabra(palabra_consultada):
  file = open("sopa.txt","r")
  numero_de_linea = 1
  for linea in file.readlines():
    print("Estoy revisando la linea",numero_de_linea)
    if palabra_consultada in linea.lower():
      return numero_de_linea
    numero_de_linea+=1
  
  return -1
  print("No se encontro la palabra")
  print(EncontrarPalabra(casa,cra,aro))
           