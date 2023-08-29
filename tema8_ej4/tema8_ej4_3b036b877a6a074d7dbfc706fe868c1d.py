def rot13(palabra):
    palabra=list(palabra)
    la=list(palabra)
    b=len(la)-1
    while b>=0:
        if la[b]=="a":
            la[b]='n'
        elif la[b]=="n":
            la[b]='a'
        elif la[b]=="b":
            la[b]='o'
        elif la[b]=="o":
            la[b]='b'
        elif la[b]=="c":
            la[b]='p'
        elif la[b]=="p":
            la[b]='c'
        elif la[b]=="d":
            la[b]='q'
        elif la[b]=="q":
            la[b]='d'
        elif la[b]=="e":
            la[b]='r'
        elif la[b]=="r":
            la[b]='e'
        elif la[b]=="f":
            la[b]='s'
        elif la[b]=="s":
            la[b]='f'
        elif la[b]=="g":
            la[b]='t'
        elif la[b]=="t":
            la[b]='g'
        elif la[b]=="h":
            la[b]='u'
        elif la[b]=="u":
            la[b]='h'
        elif la[b]=="i":
            la[b]='v'
        elif la[b]=="v":
            la[b]='i'
        elif la[b]=="j":
            la[b]='w'
        elif la[b]=="w":
            la[b]='j'
        elif la[b]=="k":
            la[b]='x'
        elif la[b]=="x":
            la[b]='k'
        elif la[b]=="l":
            la[b]='y'
        elif la[b]=="y":
            la[b]='l'
        elif la[b]=="m":
            la[b]='z'
        elif la[b]=="z":
            la[b]='m'
        b=b-1

    la="".join(la)
    return(la)
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)

