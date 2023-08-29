def decodificar(mensaje):
    deco = mensaje
    lista = []
    for mensaje in lista:
        espacio = ' '.join(format(ord(lista), 'b') for x in mensaje)
    return mensaje

if __name__ == "__main__":
    f = decodificar("01101000,01101111,01101100,01100001")
    print(f)
         