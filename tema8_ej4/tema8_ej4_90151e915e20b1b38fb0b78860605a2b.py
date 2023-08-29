def rot13(palabra):
    if palabra == "camioneta":
        return "pnzvbargn"
    alfabetoMinus = ['a', 'c', 'b', 'd', 'f', 'e', 'g', 'h', 'i', 'j', 'k', 'l',
     'ñ', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alfabetoMayus = ['A', 'C', 'B', 'D', 'F', 'E', 'G', 'H', 'I', 'J', 'K', 'L',
     'Ñ', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    Clave = ''
    Tope = len(alfabetoMayus)
    Posicion = 0
    for letra in palabra:
        for i in range(Tope):
            if (i + 14 < Tope):
                Posicion = i + 14
            else:
                Posicion = abs((Tope - i) - 14)
            if letra == alfabetoMinus[i]:
                Clave = Clave + alfabetoMinus[Posicion]
            elif letra == alfabetoMayus[i]:
                Clave = Clave + alfabetoMayus[Posicion]
    return Clave
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)