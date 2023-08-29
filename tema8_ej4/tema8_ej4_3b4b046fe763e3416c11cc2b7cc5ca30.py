def rot13(palabra):
    letras=[]
    for i in palabra:
        letras.append(i)
    palabra=''
    for i in letras:
        if i=='a':
            palabra=palabra+'n'
        elif i=='b':
            palabra=palabra+'o'
        elif i=='c':
            palabra=palabra+'p'
        elif i=='d':
            palabra=palabra+'q'
        elif i=='e':
            palabra=palabra+'r'
        elif i=='f':
            palabra=palabra+'s'
        elif i=='g':
            palabra=palabra+'t'
        elif i=='h':
            palabra=palabra+'u'
        elif i=='i':
            palabra=palabra+'v'
        elif i=='j':
            palabra=palabra+'w'
        elif i=='k':
            palabra=palabra+'x'
        elif i=='l':
            palabra=palabra+'y'
        elif i=='m':
            palabra=palabra+'z'
        elif i=='n':
            palabra=palabra+'a'
        elif i=='o':
            palabra=palabra+'b'
        elif i=='p':
            palabra=palabra+'c'
        elif i=='q':
            palabra=palabra+'d'
        elif i=='r':
            palabra=palabra+'e'
        elif i=='s':
            palabra=palabra+'f'
        elif i=='t':
            palabra=palabra+'g'
        elif i=='u':
            palabra=palabra+'h'
        elif i=='v':
            palabra=palabra+'i'
        elif i=='w':
            palabra=palabra+'j'
        elif i=='x':
            palabra=palabra+'k'
        elif i=='y':
            palabra=palabra+'l'
        elif i=='z':
            palabra=palabra+'m'
    return palabra
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           