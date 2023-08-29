def decodificador(mensaje):
  decimal = 0
  contador = 0
  potencia = len(mensaje) - 1
  
  while len(mensaje) != contador:
    decimal += int(mensaje[contador]) * (2**potencia)
    contador += 1
    potencia -= 1  

  
  return decimal  


def decodificar(mensaje):
    lista = []
    suma = ""

    for a in mensaje:
        if a != ",":
            suma += a
        elif a == ",":
            lista.append(suma)
            suma = ""
    lista.append(suma)


    mensaje = ""

    for n in lista:
        num = decodificador(n)
        mensaje += chr(num)
        
    return mensaje

if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         