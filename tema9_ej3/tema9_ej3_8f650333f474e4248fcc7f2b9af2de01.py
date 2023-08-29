def decodificar(mensaje):
    letra = ""
    palabra = ""
    for n in mensaje:
        letra += n
        if letra == "01101000,":
            palabra += "h"
            letra = ""
        elif letra == "01101111,":
            palabra += "o"
            letra = ""
        elif letra == "01101100,":
            palabra += "l"
            letra = ""
        elif letra == "01100001":
            palabra += "a"
    mensaje = palabra
    return mensaje


if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
