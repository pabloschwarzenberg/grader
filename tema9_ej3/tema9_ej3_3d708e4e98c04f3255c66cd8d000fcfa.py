def decodificar(mensaje):
    bins = mensaje.split(",")
    final = ""
    for x in bins:
        b2 = int(x, 2)
        char = chr(b2)
        final += char
    return final

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)