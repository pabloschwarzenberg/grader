def rot13(palabra):
    import string
    rot13=''
    letra=0
    while letra<len(palabra):
        new_letra=string.ascii_lowercase.index(palabra[letra])
        rot_13=new_letra+13
        if rot_13>=len(string.ascii_lowercase):
            rot_13=rot_13-26
        rot13=rot13+string.ascii_lowercase[rot_13]
        letra=letra+1
    return rot13


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           