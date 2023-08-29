abc='abcdefghijklmnñopqrstuvwxyz'

def cifrado(cadena , clave):
    text_cifrado = ''

    for letra in cadena:
        suma=abc.find(letra)+clave
        modulo=int(suma) % len(abc)
        text_cifrado = text_cifrado + str (abc[modulo])

    return text_cifrado

def decifrar( cadena , clave):
    text_cifrado=''
    for letra in cadena:
        suma=abc.find(letra)+clave
        modulo=int(suma) % len (abc)
        text_cifrado=text_cifrado+str(abc[modulo])

    return text_cifrado

def mai():
    c=str(input('cadena cifrada')).lower()
    n=int(input('clave numerica:'))
    print(cifrado(c,n))
    cc=str(input('cadena a secifrar')).lower()
    cn=int(input('clave numerica'))
    print(decifrar(c,cn))


if __name__=='__main__':
    main()
    