#Soy Oscar Páez
def rot13(palabra):
    Abecedario= "abcdefghijklmñnopqrstuvwxyz"
    encriptada = ""
    for i in palabra:
        if i in Abecedario:
            if Abecedario.index(i) < 14:
                encriptada += Abecedario[Abecedario.index(i) + 14]
            else:   
                encriptada += Abecedario[Abecedario.index(i) - 14]

        elif i in Abecedario.upper():
                if Abecedario.upper() < 14:
                    encriptada += Abecedario.upper()[Abecedario.upper().index(i) + 14]
                else:
                    encriptada += Abecedario.upper()[Abecedario.upper().index(i) - 14]
        else:
            encriptada += i
    return encriptada

print(rot13("hola"))


           