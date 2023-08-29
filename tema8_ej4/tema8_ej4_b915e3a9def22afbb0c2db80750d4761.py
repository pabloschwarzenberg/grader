def rot13(palabra):
    pal1='abcdefghijklm'
    pal2='nopqrstuvwxyz'
    zzzz=dict(zip(pal1+pal2, pal2+pal1))
    return ''.join(zzzz.get(x.lower(), x) for x in palabra)
    pass

if __name__=="__main__":
    codigo=input("ingresa el codigo que quieras cifrar: ")
    cifrado=rot13(codigo)
    print("el resultado es: ",cifrado)