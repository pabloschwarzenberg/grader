def decodificar(mensaje):
  lista = mensaje.split(",")
  decripted = ""
  for i in range(0,len(lista)):
    numero = lista[i]
    decimal = int(numero,2)
    letra = chr(decimal)
    decripted += letra
  return decripted

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         