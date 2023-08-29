def decodificar(codigo):
    codigo = codigo.split(",")
    mensaje = ""

    for digitos in codigo:
        n = 0
        for i in range(len(digitos)):
            n += int(digitos[i]) * 2**(7-i)
        mensaje += chr(n)
    
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)