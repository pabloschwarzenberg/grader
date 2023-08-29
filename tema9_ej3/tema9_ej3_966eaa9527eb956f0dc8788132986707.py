def decodificar(mensaje):
    mensaje = mensaje.split(',')
    mensaje_dec = ''
    for i in mensaje:
        bin = 0
        k = len(i)-1
        pos = 0
        print(i)
        while k > 0:
            bin+= int(i[k])*2**(pos)
            pos += 1
            k -= 1
        mensaje_dec += chr(bin)
    return mensaje_dec
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         