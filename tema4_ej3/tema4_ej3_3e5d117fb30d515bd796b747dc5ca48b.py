def jerigonzo(string):
    palabra = list(string)
    for i in palabra:
        if ['a','e','i','o','u','A','E','I','O','U'].count(i) == 1:
            palabra[palabra.index(i)] = i + 'p' + i.lower()
    palabra = ''.join(palabra)
    return palabra

if __name__ == "__main__":
    pass
         