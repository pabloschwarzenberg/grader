def decodificar(mensaje):
    mensaje = mensaje.split(",")
    newMensaje = []
    for b in mensaje:
        b = list(b)
        B1 = b[0]
        Bresto = b[1:]
        Bresto.reverse()
        Bresto.append("b")
        Bresto.append(B1)
        Bresto.reverse()
        b = "".join(Bresto)
        newMensaje.append(chr(int(b,2)))
    return "".join(newMensaje)
    
if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         