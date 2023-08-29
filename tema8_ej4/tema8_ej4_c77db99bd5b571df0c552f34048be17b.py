def rot13(palabra):
    abc='abcdefghijklmnopqrstuvwxyz'
    resultado=''
    for letra in palabra:
        if letra in abc:
            pos=abc.index(letra)+13
            if pos>=len(abc):
                pos-=len(abc)
            resultado+=abc[pos]
        else:
            resultado+=letra
    return resultado
if __name__=='__main__':
    palabra=input('Ingresa la palabra que quieras encriptar: ')
    palabra=palabra.lower()
    resultado=rot13(palabra)
    print('El resultado es:',resultado)

