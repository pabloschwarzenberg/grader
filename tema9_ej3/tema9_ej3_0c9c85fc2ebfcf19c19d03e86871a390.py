def decodificar(mensaje):
    numero_decimal1 = 0
    numero_decimal2 = 0
    numero_decimal3 = 0
    numero_decimal4 = 0
    primero = mensaje[0:8]
    segundo = mensaje[9:17]
    tercero = mensaje[18:26]
    cuarto = mensaje[27:35]

    for posicion, digito_string in enumerate(primero[::-1]):
        numero_decimal1 += int(digito_string) * 2 ** posicion

    for posicion, digito_string in enumerate(segundo[::-1]):
        numero_decimal2 += int(digito_string) * 2 ** posicion

    for posicion, digito_string in enumerate(tercero[::-1]):
        numero_decimal3 += int(digito_string) * 2 ** posicion

    for posicion, digito_string in enumerate(cuarto[::-1]):
        numero_decimal4 += int(digito_string) * 2 ** posicion

    palabra=""
    if numero_decimal1==104:
        palabra+="h"
    if numero_decimal2==111:
        palabra+="o"
    if numero_decimal3==108:
        palabra+="l"
    if numero_decimal4 == 97:
        palabra+="a"
    return palabra

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
