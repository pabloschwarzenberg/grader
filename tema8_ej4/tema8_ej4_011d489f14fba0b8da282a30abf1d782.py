def rot13(s):
    letras = "abcdefghijklmnopqrstuvwxyz"
    trans = letras[13:]+letras[:13]
    rot = lambda h: trans[letras.find(h)] if letras.find(h)>-1 else h
    return ''.join( rot(h) for h in s )

#a=input("codigo: ")
#print(rot13(a))
