def decodificar(mensaje):
    lista = []
    palabra = ""
    mensaje = mensaje + ","
    for i in mensaje:
      palabra = palabra + i
      if i == ",":
        final = palabra[:-1]
        lista.append(final)
        palabra = ""    
    palabra2 = ""
    for h in lista:
      co = len(h)-1
      total = 0
      for elemento in h:
        #multiplicar cada dígito del número binario por 2 elevado a la posición del dígito
        c = int(elemento)
        decimal = c * 2** co
        co-= 1
        total = total + decimal
      palabra2 = palabra2 + chr(total)   
    return palabra2

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         