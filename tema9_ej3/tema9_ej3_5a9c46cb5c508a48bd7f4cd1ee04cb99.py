def decodificar(mensaje):
    listaBin = mensaje.split(',')
    listaDec = []
    listaChr = []
    for i in listaBin:
      listaDec.append(int(i,2))
    for i in listaDec:
      listaChr.append(chr(i))
    mensaje = ''.join(listaChr)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         