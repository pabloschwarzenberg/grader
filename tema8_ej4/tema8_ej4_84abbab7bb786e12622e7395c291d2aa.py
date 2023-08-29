#Rot-13
def rot13(palabra):
    palabra=list(palabra)
    for n in range(0,len(palabra)):
        if palabra[n]=='a':
            palabra[n]='n'
        elif palabra[n]=='b':
            palabra[n]='o'
        elif palabra[n]=='c':
            palabra[n]='p'
        elif palabra[n]=='d':
            palabra[n]='q'
        elif palabra[n]=='e':
            palabra[n]='r'
        elif palabra[n]=='f':
            palabra[n]='s'
        elif palabra[n]=='g':
            palabra[n]='t'
        elif palabra[n]=='h':
            palabra[n]='u'
        elif palabra[n]=='i':
            palabra[n]='v'
        elif palabra[n]=='j':
            palabra[n]='w'
        elif palabra[n]=='k':
            palabra[n]='x'
        elif palabra[n]=='l':
            palabra[n]='y'
        elif palabra[n]=='m':
            palabra[n]='z'
        elif palabra[n]=='n':
            palabra[n]='a'
        elif palabra[n]=='o':
            palabra[n]='b'
        elif palabra[n]=='p':
            palabra[n]='c'
        elif palabra[n]=='q':
            palabra[n]='d'
        elif palabra[n]=='r':
            palabra[n]='e'
        elif palabra[n]=='s':
            palabra[n]='f'
        elif palabra[n]=='t':
            palabra[n]='g'
        elif palabra[n]=='u':
            palabra[n]='h'
        elif palabra[n]=='v':
            palabra[n]='i'
        elif palabra[n]=='w':
            palabra[n]='j'
        elif palabra[n]=='x':
            palabra[n]='k'
        elif palabra[n]=='y':
            palabra[n]='l'
        elif palabra[n]=='z':
            palabra[n]='m'
    palabra=''.join(palabra)
    return palabra
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           