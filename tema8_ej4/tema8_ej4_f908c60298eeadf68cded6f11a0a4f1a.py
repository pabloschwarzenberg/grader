def rot13(s):
    chars = "abcdefghijklmnopqrstuvwxyz"
    pov = chars[13:]+chars[:13]
    rot_char = lambda c: pov[chars.find(c)] if chars.find(c)>-1 else c
    return ''.join( rot_char(c) for c in s ) 


           