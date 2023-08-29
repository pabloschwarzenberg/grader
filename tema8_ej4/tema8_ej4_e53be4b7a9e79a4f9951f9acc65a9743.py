def rot13(palabra):
    prp=""
    for x in palabra:
        if ord(x) in range(97, 110):
            prp = prp+(chr(ord(x)+13))
        elif ord(x) in range(110, 123):
            prp = prp+(chr(ord(x)-13))
    return prp        