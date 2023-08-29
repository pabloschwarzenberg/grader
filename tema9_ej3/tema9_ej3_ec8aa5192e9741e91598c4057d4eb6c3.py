def decodificar(texto):
    binario = texto.split(",")
    decimal = []
    for num in binario:
        decimal.append(int(num, 2))
    caracteres = []
    for num in decimal:
        caracteres.append(chr(num))
    return "".join(caracteres)

decodificar("01101000,01101111,01101100,01100001")