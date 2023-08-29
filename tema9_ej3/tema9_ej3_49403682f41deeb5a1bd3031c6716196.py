def decodificar(mensaje):
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
def decodificar(mensaje):
    LetraBinario = mensaje.split(',')
    LetraDecimal = []
    final = ''
    a = 0
    while a < len(LetraBinario):
        suma = 0
        exp = 7
        for elemento in LetraBinario[a]:
            suma += int(elemento)*(2**exp)
            exp -= 1
        LetraDecimal.append(suma)
        a += 1

    for letra in LetraDecimal:
        final += chr(letra)


    return final

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)