def rot13(palabra):
    nuevo = ''
    for i in palabra:
        if i == 'z':
            nuevo = nuevo + 'm'
        if i == 'y':
            nuevo = nuevo + 'l'
        if i == 'x':
            nuevo = nuevo + 'k'
        if i == 'w':
            nuevo = nuevo + 'j'
        if i == 'v':
            nuevo = nuevo + 'i'
        if i == 'u':
            nuevo = nuevo + 'h'
        if i == 't':
            nuevo = nuevo + 'g'
        if i == 's':
            nuevo = nuevo + 'f'
        if i == 'r':
            nuevo = nuevo + 'e'
        if i == 'q':
            nuevo = nuevo + 'd'
        if i == 'p':
            nuevo = nuevo + 'c'
        if i == 'o':
            nuevo = nuevo + 'b'
        if i == 'n':
            nuevo = nuevo + 'a'
        if i == 'a':
            nuevo = nuevo + 'n'
        if i == 'b':
            nuevo = nuevo + 'o'
        if i == 'c':
            nuevo = nuevo + 'p'
        if i == 'd':
            nuevo = nuevo + 'q'
        if i == 'e':
            nuevo = nuevo + 'r'
        if i == 'f':
            nuevo = nuevo + 's'
        if i == 'g':
            nuevo = nuevo + 't'
        if i == 'h':
            nuevo = nuevo + 'u'
        if i == 'i':
            nuevo = nuevo + 'v'
        if i == 'j':
            nuevo = nuevo + 'w'
        if i == 'k':
            nuevo = nuevo + 'x'
        if i == 'l':
            nuevo = nuevo + 'y'
        if i == 'm':
            nuevo = nuevo + 'z'

    return nuevo