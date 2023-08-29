def decodificar(mensaje):
    mensaje_n = list(mensaje)
    for i in mensaje_n:
        if i == ",":
            mensaje_n.remove(i)
    mensaje_n =  str("".join(mensaje_n))
    
    return ''.join(chr(int(mensaje_n[i*8:i*8+8],2)) for i in range(len(mensaje_n)//8))



if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         