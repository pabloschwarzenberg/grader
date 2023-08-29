def rot13(x):
    character = "abcdefghijklmnopqrstuvwxyz"
    trans = character[13:]+character[:13]
    rot_character = lambda c: trans[character.find(c)] if character.find(c)>-1 else c
    return ''.join( rot_character(c) for c in x )