def rot13(palabra):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    cifrado = abecedario[13:] + abecedario [:13]
    encriptar = lambda a: cifrado[abecedario.find(a)] if abecedario.find (a) > -1 else a
    return "".join(encriptar(a) for a in palabra)
    pass
