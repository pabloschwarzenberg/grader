def jerigonzo(string):
    texto_modificado = ""
    i = 0
    while i < len(string):
        if string[i] == "a":
            texto_modificado += string[i] + str("p")
        if string[i] == "e":
            texto_modificado += string[i] + str("p")
        if string[i] == "i":
            texto_modificado += string[i] + str("p")
        if string[i] == "o":
            texto_modificado += string[i] + str("p")
        if string[i] == "u":
            texto_modificado += string[i] + str("p")
        else:
            texto_modificado += string[i]
        i += 1
    return texto_modificado
#    return string
#    print(string)

if __name__ == "__main__":
    texto = str(input("Ingrese texto: "))
    print(jerigonzo(texto))
    pass
         