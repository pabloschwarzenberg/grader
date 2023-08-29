def decodificar(mensaje):
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
def decodificar(mensaje):
    md = "" # mensaje decodificado
    cb = "" # cadena binaria
    for c in mensaje:
        if c!=",":
            cb = cb + c # conformar la cadena binaria
        else:
            ord_car = int(cb,2) # ordinal del caracter (código Ascii)
            md = md + chr(ord_car) # conformar el mensaje decodificado
            cb = "" # reiniciar el acumulador de digitos binarios
    # Al terminar el for la última cadena binaria no se transforma
    ord_car = int(cb,2) # ordinal del ultimo caracter (código Ascii)
    md = md + chr(ord_car) # conformar el mensaje decodificado con el ultimo caracter
    return md