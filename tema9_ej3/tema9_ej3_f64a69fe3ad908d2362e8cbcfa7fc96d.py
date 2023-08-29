def decodificar(mensaje):
    Lbi = mensaje.split(',')
    Ldeci = []
    final = ''
    a = 0
    while a < len(Lbi):
        suma = 0
        exp = 7
        for elemento in Lbi[a]:
            suma += int(elemento)*(2**exp)
            exp -= 1
        Ldeci.append(suma)
        a += 1

    for letra in Ldeci:
        final += chr(letra)


    return final

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         