def decodificar(mensaje):
    md = "" # mensaje decodificado - acumulador de caracteres
    cb = "" # subcadena binaria
    for c in mensaje:
        if c!=",":
            cb = cb + c # conformo la subcadena binaria
        else:
            ord_car = int(cb,2) # se determina el ordinal del caracter
            md = md + chr(ord_car) # conformando la cadena de caracteres decodificada
            cb = "" # reiniciar el acumulador de caracteres binarios
    # Al terminar el ciclo for queda sin procesar la última
    # subcadena binaria
    ord_car = int(cb,2) # se determina el ordinal de la ultima subcadena binaria
    md = md + chr(ord_car) # se concatena al final de la cadena decodificada
    return md

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         