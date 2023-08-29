def decodificar(mensaje):
    x=mensaje.split(",")
    y=[]
    z=[]
    for i0 in x:
      i0=int(i0,2)
      y.append(i0)

    for i1 in y:
      i1=chr(i1)
      z.append(i1)

    resultado="".join(z)
    return (resultado)

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         