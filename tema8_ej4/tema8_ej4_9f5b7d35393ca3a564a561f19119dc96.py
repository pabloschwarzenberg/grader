def rot13(palabra):
    frase=''
    for letra in palabra:
        if 'a'<=letra<='m' or 'A'<=letra<='M':
            l=ord(letra)+13
            frase=frase+chr(l)
        if 'n'<=letra<='z' or 'N'<=letra<='Z':
            l=ord(letra)-13
            frase=frase+chr(l)
    return frase     