def decodificar(mensaje):
    mensaje = mensaje.split(",")
    palabra = ""
    for bin in mensaje:
        num_bin = bin
        dec = int(num_bin, 2)
        dec = chr(dec)
        palabra += dec

    return palabra
if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
