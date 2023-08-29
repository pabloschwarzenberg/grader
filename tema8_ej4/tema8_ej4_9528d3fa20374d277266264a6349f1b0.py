s = ' nonono'
def cod(s):
    letras = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    trans = letras[26:]+letras[:26]
    rot_char = lambda c: trans[letras.find(c)] if letras.find(c) > -1 else c
    c = ''.join(rot_char(c) for c in s)
    
    return c

print(cod(s))