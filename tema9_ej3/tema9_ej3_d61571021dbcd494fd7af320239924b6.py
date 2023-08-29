def decodificar(mensaje):
    cod = []
    mensaje = [str(x) for x in mensaje if x != ',']
    mensaje = ''.join([str(x) for x in mensaje])
    w = 8
    final = [mensaje[i * w:(i + 1) * w] for i in range((len(mensaje) + w- 1) // w )] 

    def binario_a_decimal(numero_binario):
        numero_decimal = 0 
        for posicion, digito_string in enumerate(numero_binario[::-1]):
            numero_decimal += int(digito_string) * 2 ** posicion
        return(numero_decimal)

    for x in range(len(final)):
        a = (binario_a_decimal(final[x]))
        cod.append(chr(a))
        print(cod)
    cod = ''.join([str(x) for x in cod])
    return(cod)

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         