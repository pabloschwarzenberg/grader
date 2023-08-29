def decodificar(mensaje):
    lista = mensaje.split(",")
    mensaje = ""
    for elemento in lista:
        elemento = list(elemento)
        elemento.reverse()
        elemento = "".join(elemento)
        n = 0
        for i in range(len(elemento)):
            if elemento[i] == "1":
                n += 2**i           
        mensaje += chr(n)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         