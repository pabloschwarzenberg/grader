def decodificar(mensaje):
  lista=[]
  palabrafinal=""
  mensaje=mensaje.split(",")

  for decimal in mensaje:
    suma=0
    for largo in range(len(decimal)):
      suma+=(int(decimal[-1-largo])*((2)**(largo)))
    lista.append(suma)

  for letra in lista:
    palabrafinal+=(chr(letra))
  return palabrafinal