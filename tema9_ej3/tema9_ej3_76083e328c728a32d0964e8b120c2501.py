def decodificar(mensaje):
  mensaje1 = mensaje[0:8]
  mensaje2 = mensaje[10:17]
  mensaje3 = mensaje[19:26]
  mensaje4 = mensaje[27:35]
  listamensajes=[mensaje1, mensaje2, mensaje3, mensaje4]
  palabra=""
  for i in listamensajes:
    decimal = int(str(i),2)
    carac = chr(decimal)
    palabra = palabra + str(carac)
  return palabra

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         