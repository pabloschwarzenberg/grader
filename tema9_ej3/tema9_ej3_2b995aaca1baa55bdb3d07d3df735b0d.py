def decodificar(mensaje):
    m=mensaje.split(",")
    r1=[]
    r2=[]
    r3=""
    for a in m:
      r1.append(int(a,2))
    for a in r1:
      r2.append(chr(a))
    for a in r2:
      r3+=a
    return r3

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         