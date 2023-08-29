#def rot13(palabra):
#    pass

#if __name__=="__main__":
#    palabra=input("Ingresa la palabra que quieras encriptar: ")
#    palabra.lower()
#    resultado=rot13(palabra)
#    print("El resultado es: ",resultado)
def rot13(x):
    lista=('')
    for i in x:
        #lista=('')
        if i=='a':
            i='n'
            lista+=i
        elif i=='b':
            i='o'
            lista+=i
        elif i=='c':
            i='p'
            lista+=i
        elif i=='d':
            i='q'
            lista+=i
        elif i=='e':
            i='r'
            lista+=i
        elif i=='f':
            i='s'
            lista+=i
        elif i=='g':
            i='t'
            lista+=i
        elif i=='h':
            i='u'
            lista+=i
        elif i=='i':
            i='v'
            lista+=i
        elif i=='j':
            i='w'
            lista+=i
        elif i=='k':
            i='x'
            lista+=i
        elif i=='l':
            i='y'
            lista+=i
        elif i=='m':
            i='z'
            lista+=i
        elif i=='n':
            i='a'
            lista+=i
        elif i=='o':
            i='b'
            lista+=i
        elif i=='p':
            i='c'
            lista+=i
        elif i=='q':
            i='d'
            lista+=i
        elif i=='r':
            i='e'
            lista+=i
        elif i=='s':
            i='f'
            lista+=i
        elif i=='t':
            i='g'
            lista+=i
        elif i=='u':
            i='h'
            lista+=i
        elif i=='v':
            i='i'
            lista+=i
        elif i=='w':
            i='j'
            lista+=i
        elif i=='x':
            i='k'
            lista+=i
        elif i=='y':
            i='l'
            lista+=i
        elif i=='z':
            i='m'
            lista+=i
        
    return lista
           