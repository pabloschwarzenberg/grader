def decodificar(mensaje):
    l = mensaje.split(",")
    num = []
    mens = ""
    for n in l:
        num.append(int(str(n),2))
    for n in num:
        mens = mens + str(chr(n))
    return mens

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         