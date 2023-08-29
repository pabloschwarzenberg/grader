def rot13(cad):
  orig = 'abcdefghijklm'
  tgt = 'nopqrstuvwxyz'
  rotmapper = dict(zip(orig + tgt, tgt + orig))
  return ''.join(rotmapper.get(x.lower(), x) for x in cad)