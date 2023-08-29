def rot_13(cad):
    pass
    a = 'ABCDEFGHIJKLM'
    b = 'NOPQRSTUVWXYZ'
    rotmapper = dict(zip(a + b, b + a))
    return ''.join(rotmapper.get(x.upper(), x) for x in cad)
print(rot_13("ryclgubavfgn"))
           