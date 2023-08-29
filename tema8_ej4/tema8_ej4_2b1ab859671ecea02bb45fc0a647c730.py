import string

def make_rot_n(n):
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    trans = str.maketrans(lc + uc,
                          lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: str.translate(s, trans)

rot13 = make_rot_n(13)

rot13('foobar') 
           