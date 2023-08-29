def rot_13(cad):
     orig = 'ABCDEFGHIJKLM'
     tgt = 'NOPQRSTUVWXYZ'
     rotmapper = dict(zip(orig + tgt, tgt + orig))
     return ''.join(rotmapper.get(x.upper(), x) for x in cad)