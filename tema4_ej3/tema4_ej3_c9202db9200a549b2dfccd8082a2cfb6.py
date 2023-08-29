def jerigonzo(string):
    jerigonzo = []
    for p in string:
        for l in p:
            vocales = 'aiueoAIUEO'
            if l in vocales:
                l = l + 'p' + l
            jerigonzo.append(l)
    unido = ''.join(jerigonzo)
    string = unido
    return string