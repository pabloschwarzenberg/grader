def decodificar(mensaje):
    nd = 0
    
    for posicion, digito_string in enumerate(mensaje[:-1]):
        nd = nd + int(digito_string) * 2 ** posicion
    return nd

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         