def binary_to_txt(msj):
    position = 0
    decimal = 0
    binary = msj[::-1]
    for digit in binary:
        multiplication = 2 ** position
        decimal += int(digit) * multiplication
        position += 1
    character = (chr(decimal))
    return character

def decodificar(mensaje):
    codi = mensaje.split(",")
    txt = ""
    res  = ""
    for c in codi:
        res  = binary_to_txt(c)
        txt = txt + res
    return txt

if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
