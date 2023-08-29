#Creador: Daniel Ugarte
def rot13(s):
    alf = "abcdefghijklmnopqrstuvwxyz"
    trns = alf[13:]+alf[:13]
    rot_char = lambda c: trns[alf.find(c)] if alf.find(c)>-1 else c
    return ''.join( rot_char(c) for c in s ) 
           