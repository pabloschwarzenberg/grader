def decodificar(mensaje):
    mensajefinal=""
    numeros=list(mensaje.split(","))
    for i in numeros:
      numero=list(i)
      numeroletra=0
      x=7
      while x>=0:
        numeroletra += int(numero[x])*(2**(7-x))
        x = x-1
      mensajefinal += chr(numeroletra)
    return mensajefinal

mensaje=decodificar("01101000,01101111,01101100,01100001")
print(mensaje)
         