def rot13(palabra):
    palabra.lower()
    char13_1="abcdefghijklm"
    char13_2="nopqrstuvwxyz"
    letra13=""
    palabra13=""
    for letra in palabra:
        aux=int(0)
        if ord(letra)>=97 and ord(letra)<=109:
            aux=ord(letra)-97
            letra13=char13_2[aux]
        elif ord(letra)>=110 and ord(letra)<=122:
            aux=ord(letra)-110
            letra13=char13_1[aux]
        palabra13+=letra13
    return palabra13
           