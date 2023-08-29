def decodificar(s):
    y = s.split(",")
    j = ''.join(y)


    mensaje = ''.join(chr(int(j[i*8:i*8+8],2)) for i in range(len(j)//8))
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         