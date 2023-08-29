def decodificar(mensaje):
    mensaje = mensaje.split(",")
    respuesta = ""
    for secuencia in mensaje:
      i = -1
      pot = 0
      decimal = 0
      while i>=len(secuencia)*-1:
        decimal+=2**pot*int(secuencia[i])
        pot+=1
        i-=1
      respuesta+= chr(decimal)
    return respuesta

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         