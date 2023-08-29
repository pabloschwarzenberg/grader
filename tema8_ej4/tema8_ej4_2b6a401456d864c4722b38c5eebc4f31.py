import math
def rot13(cad):
     orig = 'ABCDEFGHIJKLM'
     tgt = 'NOPQRSTUVWXYZ'
     rotmapper = dict(zip(orig + tgt, tgt + orig))
     return ''.join(rotmapper.get(x.upper(), x) for x in cad)

rot13('hola')
'ubyn'
rot13('camioneta')
'pnzvbargn'
rot13('zorro')
'mbeeb'