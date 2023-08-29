def rot13(s):
    s_rot13 = ''
    for i in range(len(s)):
        if s[i] == 'a':
            s_rot13 = s_rot13 + 'n'
        elif s[i] == 'b':
            s_rot13 = s_rot13 + 'o'
        elif s[i] == 'c':
            s_rot13 = s_rot13 + 'p'
        elif s[i] == 'd':
            s_rot13 = s_rot13 + 'q'
        elif s[i] == 'e':
            s_rot13 = s_rot13 + 'r'
        elif s[i] == 'f':
            s_rot13 = s_rot13 + 's'
        elif s[i] == 'g':
            s_rot13 = s_rot13 + 't'
        elif s[i] == 'h':
            s_rot13 = s_rot13 + 'u'
        elif s[i] == 'i':
            s_rot13 = s_rot13 + 'v'
        elif s[i] == 'j':
            s_rot13 = s_rot13 + 'w'
        elif s[i] == 'k':
            s_rot13 = s_rot13 + 'x'
        elif s[i] == 'l':
            s_rot13 = s_rot13 + 'y'
        elif s[i] == 'm':
            s_rot13 = s_rot13 + 'z'
        elif s[i] == 'n':
            s_rot13 = s_rot13 + 'a'
        elif s[i] == 'o':
            s_rot13 = s_rot13 + 'b'
        elif s[i] == 'p':
            s_rot13 = s_rot13 + 'c'
        elif s[i] == 'q':
            s_rot13 = s_rot13 + 'd'
        elif s[i] == 'r':
            s_rot13 = s_rot13 + 'e'
        elif s[i] == 's':
            s_rot13 = s_rot13 + 'f'
        elif s[i] == 't':
            s_rot13 = s_rot13 + 'g'
        elif s[i] == 'u':
            s_rot13 = s_rot13 + 'h'
        elif s[i] == 'v':
            s_rot13 = s_rot13 + 'i'
        elif s[i] == 'w':
            s_rot13 = s_rot13 + 'j'
        elif s[i] == 'x':
            s_rot13 = s_rot13 + 'k'
        elif s[i] == 'y':
            s_rot13 = s_rot13 + 'l'
        elif s[i] == 'z':
            s_rot13 = s_rot13 + 'm'
        else:
            s_rot13 = s_rot13 + s[i]
    return s_rot13

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           