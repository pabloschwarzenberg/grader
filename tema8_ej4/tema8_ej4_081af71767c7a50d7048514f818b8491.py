def rot13(palabra):
    n = 13
    Lista = list(palabra)
    lstcode = []
    for letra in Lista:
        if letra.isalpha():
            if "A" <= letra <= "Z":
                lstcode.append(chr((ord(letra)-65+n)%26+65))
            else:
                lstcode.append(chr((ord(letra)-97+n)%26+97))
        elif letra.isdigit():
            lstcode.append(chr((int(letra)+n)%10+48))

    strcode = "".join(lstcode)
    return(strcode)


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           