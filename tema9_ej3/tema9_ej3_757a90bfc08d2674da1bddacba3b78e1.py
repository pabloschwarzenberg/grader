def decodificar(mensaje):
    uwu3 = []
    ayuda = []
    uwu1 = list(mensaje)
    for a in uwu1:
        if a == ",":
            uwu4 = "".join(ayuda)
            uwu3.append(uwu4)
            ayuda = []
        else:
            ayuda.append(a)
    uwu4 = "".join(ayuda)
    uwu3.append(uwu4)
    ayuda = []
    for b in uwu3:
        uwu = int(b,2)
        awa = chr(uwu)
        ayuda.append(awa)
    mensaje = "".join(ayuda)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         