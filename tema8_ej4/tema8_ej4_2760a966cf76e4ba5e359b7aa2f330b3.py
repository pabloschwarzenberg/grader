def rot13(palabra):
    pc = ""
    codigo1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
    codigo2 = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for i in palabra:
        if i in codigo1:
            j = 0
            while i != codigo1[j]:
                j += 1
            pc += codigo2[j]
        if i in codigo2:
            j = 0
            while i != codigo2[j]:
                j += 1
            pc += codigo1[j]
    return pc

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)