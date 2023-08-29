def decodificar(mensaje):
    mensaje=mensaje.split(",")
    codificado=[]
    for i in range(len(mensaje)):
      a=int(mensaje[i],2)
      c=chr(a)
      codificado.append(c)
    k="".join(codificado)
    return k
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
