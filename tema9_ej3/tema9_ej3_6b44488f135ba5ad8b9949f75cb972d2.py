def decodificar(mensaje):
    binario=mensaje.split(",")
    texto=""
    for i in binario:
      code=0
      for j in range(8):
        if i[j]=="1":
          code=code+(2**(7-j))
      texto=texto+chr(int(code))
    return texto

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         