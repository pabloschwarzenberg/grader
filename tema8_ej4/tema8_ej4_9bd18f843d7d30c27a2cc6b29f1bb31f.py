def rot13(palabra):
    codigo = ''
    for i in palabra:
        if i == 'a':
            i = 'n'
            codigo += i
        elif i == 'b':
            i = 'o'
            codigo += i
        elif i == 'c':
            i = 'p'
            codigo += i
        elif i == 'd':
            i = 'q'
            codigo += i
        elif i == 'e':
            i = 'r'
            codigo += i
        elif i == 'f':
            i = 's'
            codigo += i
        elif i == 'g':
            i = 't'
            codigo += i
        elif i == 'h':
            i = 'u'
            codigo += i
        elif i == 'i':
            i = 'v'
            codigo += i
        elif i == 'j':
            i = 'w'
            codigo += i
        elif i == 'k':
            i = 'x'
            codigo += i
        elif i == 'l':
            i = 'y'
            codigo += i
        elif i == 'm':
            i = 'z'
            codigo += i
        elif i == 'n':
            i = 'a'
            codigo += i
        elif i == 'o':
            i = 'b'
            codigo += i
        elif i == 'p':
            i = 'c'
            codigo += i
        elif i == 'q':
            i = 'd'
            codigo += i
        elif i == 'r':
            i = 'e'
            codigo += i
        elif i == 's':
            i = 'f'
            codigo += i
        elif i == 't':
            i = 'g'
            codigo += i
        elif i == 'u':
            i = 'h'
            codigo +=i
        elif i == 'v':
            i = 'i'
            codigo += i
        elif i == 'w':
            i = 'j'
            codigo += i
        elif i == 'x':
            i = 'k'
            codigo += i
        elif i == 'y':
            i = 'l'
            codigo += i
        elif i == 'z':
            i = 'm'
            codigo += i
    return codigo
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           