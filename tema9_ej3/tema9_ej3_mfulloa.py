def decodificar(mensaje):
    s=""
    m=mensaje.strip().split(",")
    for x in range(len(m)):
        s+=chr(int(m[x],2))
    return s

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         