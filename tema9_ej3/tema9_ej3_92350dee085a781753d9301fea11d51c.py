def decodificar(mensaje):
  lista=mensaje.split(",")
  palabra=""
  for i in range(0, len(lista)):
      binario=(lista[i])
      entero=int(str(binario), 2)
      letra=chr(entero)
      palabra=palabra+letra
  return palabra

if __name__ == "__main__":
    palabra=decodificar("01101000,01101111,01101100,01100001")
    print(palabra)
         