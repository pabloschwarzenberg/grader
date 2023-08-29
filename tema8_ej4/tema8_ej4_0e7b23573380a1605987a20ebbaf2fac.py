def rot13(palabra):
    lista = []
    for x in palabra:
        if x == 'a':
            lista.append('n')
        if x == 'b':
            lista.append('o')
        if x == 'c':
            lista.append('p')
        if x == 'd':
            lista.append('q')
        if x == 'e':
            lista.append('r')
        if x == 'f':
            lista.append('s')
        if x == 'g':
            lista.append('t')
        if x == 'h':
            lista.append('u')
        if x == 'i':
            lista.append('v')
        if x == 'j':
            lista.append('w')
        if x == 'k':
            lista.append('x')
        if x == 'l':
            lista.append('y')
        if x == 'm':
            lista.append('z')
        if x == 'n':
            lista.append('a')
        if x == 'o':
            lista.append('b')
        if x == 'p':
            lista.append('c')
        if x == 'q':
            lista.append('d')
        if x == 'r':
            lista.append('e')
        if x == 's':
            lista.append('f')
        if x == 't':
            lista.append('g')
        if x == 'u':
            lista.append('h')
        if x == 'v':
            lista.append('i')
        if x == 'w':
            lista.append('j')
        if x == 'x':
            lista.append('k')
        if x == 'y':
            lista.append('l')
        if x == 'z':
            lista.append('m')

    lista = "".join(lista)
    return lista

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           