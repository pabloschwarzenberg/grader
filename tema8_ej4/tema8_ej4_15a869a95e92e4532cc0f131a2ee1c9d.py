def rot13(palabra):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    s = ""
    for j in palabra:
        if j in abecedario:
            if abecedario.index(j) < 13:
                s += abecedario[abecedario.index(j) + 13]
            else:
                s += abecedario[abecedario.index(j) - 13]
        elif j in abecedario.upper():
            if abecedario.upper().index(j) < 13:
                s += abecedario[abecedario.upper().index(j) + 13]
            else:
                s += abecedario[abecedario.upper().index(j) - 13]
        else:
            s += j
    return s

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           