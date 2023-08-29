def rot13(cad):
    orig = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
    tgt = 'NOPQRSTUVWXYZABCDEFGHIJKLM'.lower()
    rotmapper = dict(zip(orig + tgt, tgt + orig))
    return ''.join(rotmapper.get(x.lower(), x) for x in cad)