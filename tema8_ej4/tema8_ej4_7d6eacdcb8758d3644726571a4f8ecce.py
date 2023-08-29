def rot13(palabra):
    palabra.lower()
    palabrak = list(palabra)
    for i in range(len(palabrak)):
        if palabrak[i] == 'a':
             palabrak[i] = 'n'
        elif palabrak[i] == 'b':
             palabrak[i] = 'o'
        elif palabrak[i] == 'c':
             palabrak[i] = 'p'
        elif palabrak[i] == 'd':
             palabrak[i] = 'q'
        elif palabrak[i] == 'e':
             palabrak[i] = 'r'
        elif palabrak[i] == 'f':
             palabrak[i] = 's'
        elif palabrak[i] == 'g':
             palabrak[i] = 't'
        elif palabrak[i] == 'h':
             palabrak[i] = 'u'
        elif palabrak[i] == 'i':
             palabrak[i] = 'v'
        elif palabrak[i] == 'j':
             palabrak[i] = 'w'
        elif palabrak[i] == 'k':
             palabrak[i] = 'x'
        elif palabrak[i] == 'l':
             palabrak[i] = 'y'
        elif palabrak[i] == 'm':
             palabrak[i] = 'z'
        elif palabrak[i] == 'n':
             palabrak[i] = 'a'
        elif palabrak[i] == 'o':
             palabrak[i] = 'b'
        elif palabrak[i] == 'p':
             palabrak[i] = 'c'
        elif palabrak[i] == 'q':
             palabrak[i] = 'd'
        elif palabrak[i] == 'r':
             palabrak[i] = 'e'
        elif palabrak[i] == 's':
             palabrak[i] = 'f'
        elif palabrak[i] == 't':
             palabrak[i] = 'g'
        elif palabrak[i] == 'u':
             palabrak[i] = 'h'
        elif palabrak[i] == 'v':
             palabrak[i] = 'i'
        elif palabrak[i] == 'w':
             palabrak[i] = 'j'
        elif palabrak[i] == 'x':
             palabrak[i] = 'k'
        elif palabrak[i] == 'y':
             palabrak[i] = 'l'
        elif palabrak[i] == 'z':
             palabrak[i] = 'm'
            
    l = "".join(palabrak)
    return (l)

if __name__ == "__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: " , resultado)