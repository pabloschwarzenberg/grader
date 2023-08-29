def rot13(palabra):
    abecedario = 'a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'q' 'r' 's' 't' 'u' 'v' 'w' 'x' 'y' 'z'
    traduccion = abecedario[13:] + abecedario[:13]
    rotar_letras = lambda i: traduccion[abecedario.find(i)] if abecedario.find(i) > -1 else i
    return ''.join(rotar_letras(c) for c in palabra)