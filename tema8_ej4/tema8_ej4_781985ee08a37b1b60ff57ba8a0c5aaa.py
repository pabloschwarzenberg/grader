import string

def make_rot_n(n):
    lowercase = string.ascii_lowercase #Devolución de cadenas en minísculas de codificación alfanumérica.
    uppercase = string.ascii_uppercase #Devolución de cadenas en mayúsculas de codificación alfanumérica.
    traduccion = str.maketrans(lowercase + uppercase, lowercase[n:] + lowercase[:n] + uppercase[n:] + uppercase[:n])
    return lambda s: str.translate(s, traduccion)

rot13 = make_rot_n(13)

rot13('foobar')
# 'sbbone'