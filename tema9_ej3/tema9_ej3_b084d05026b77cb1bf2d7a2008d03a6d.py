def decodificar(mensaje):
    mensaje = mensaje.split(",")
    mensaje_final = []
    for i in mensaje:
        mensaje_final.append(chr(binario_decimal(i)))
    mensaje = "".join(mensaje_final)
    return mensaje

def binario_decimal(numero):
    s = 0
    num = list(numero)
    num.reverse()
    for i in range(0, len(num)):
        s = s + int(num[i])*2**i
    return s

if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)