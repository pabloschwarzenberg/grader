def rot13(palabra):
    palabra2=''
    for i in palabra:
        if i=='a':
            j='n'
            palabra2=palabra2+j
        elif i=='b':
            j='o'
            palabra2=palabra2+j

        elif i=='c':
            j='p'
            palabra2=palabra2+j

        elif i=='d':
            j='q'
            palabra2=palabra2+j

        elif i=='e':
            j='r'
            palabra2=palabra2+j

        elif i=='f':
            j='s'
            palabra2=palabra2+j

        elif i=='g':
            j='t'
            palabra2=palabra2+j

        elif i=='h':
            j='u'
            palabra2=palabra2+j
        elif i=='i':
            j='v'
            palabra2=palabra2+j
        elif i=='j':
            j='w'
            palabra2=palabra2+j
        elif i=='k':
            j='x'
            palabra2=palabra2+j
        elif i=='l':
            j='y'
            palabra2=palabra2+j
        if i=='m':
            j='z'
            palabra2=palabra2+j


        if i=='n':
            j='a'
            palabra2=palabra2+j
        if i=='o':
            j='b'
            palabra2=palabra2+j

        if i=='p':
            j='c'
            palabra2=palabra2+j

        if i=='q':
            j='d'
            palabra2=palabra2+j

        if i=='r':
            j='e'
            palabra2=palabra2+j

        if i=='s':
            j='f'
            palabra2=palabra2+j

        if i=='t':
            j='g'
            palabra2=palabra2+j

        if i=='u':
            j='h'
            palabra2=palabra2+j
        if i=='v':
            j='i'
            palabra2=palabra2+j
        if i=='w':
            j='j'
            palabra2=palabra2+j
        if i=='x':
            j='k'
            palabra2=palabra2+j
        if i=='y':
            j='l'
            palabra2=palabra2+j
        if i=='z':
            j='m'
            palabra2=palabra2+j
            
    return palabra2

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           