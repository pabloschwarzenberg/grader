def decodificar(mensaje):
    mensaje = mensaje.split(",")
    palabra_cifrada = []
    for i in mensaje:
        cifrado = 0 
        exp = 7
        for k in i:
            operatoria = 2 ** exp
            if k == "0":
                cifrado += 0
            else:
                cifrado += operatoria
            exp -= 1
        letra = chr(cifrado)
        palabra_cifrada.append(letra)
        mensaje = "".join(palabra_cifrada)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         