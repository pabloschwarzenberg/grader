def rot13(palabra):
    letras = "abcdefghijklmnopqrstuvwxyz"
    x = letras[13:]+letras[:13]
    _rot13 = lambda a: x[letras.find(a)] if letras.find(a)>-1 else a
    return ''.join( _rot13(a) for a in palabra) 
