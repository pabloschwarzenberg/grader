def decodificar(mensaje):
    palabra=""
    for i in mensaje.split(","):
      b = i
      decimal =(int(str(b), 2))
      palabra+=chr(decimal)
    return palabra


         