def rot13(palabra):
    lista=[]
    for i in palabra:
        if i=='a':
            i='n'
        elif i=='b':
            i='o'
        elif i=='c':
            i='p'
        elif i=='d':
            i='q'
        elif i=='e':
            i='r'
        elif i=='f':
            i='s'
        elif i=='g':
            i='t'
        elif i=='h':
            i='u'
        elif i=='i':
            i='v'
        elif i=='j':
            i='w'
        elif i=='k':
            i='x'
        elif i=='l':
            i='y'
        elif i=='m':
            i='z'
        elif i=='n':
            i='a'
        elif i=='o':
            i='b'
        elif i=='p':
            i='c'
        elif i=='q':
            i='d'
        elif i=='r':
            i='e'
        elif i=='s':
            i='f'
        elif i=='t':
            i='g'
        elif i=='u':
            i='h'
        elif i=='v':
            i='i'
        elif i=='w':
            i='j'
        elif i=='x':
            i='k'
        elif i=='y':
            i='l'
        elif i=='z':
            i='m'
        lista.append(i)
    return lista

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower(palabra)
    resultado="".join(rot13(palabra))
    resultado=str(resultado)
    print("El resultado es: ",resultado)