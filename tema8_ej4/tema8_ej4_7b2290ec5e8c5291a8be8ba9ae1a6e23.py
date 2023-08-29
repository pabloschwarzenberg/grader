def rot13(palabra):
    
     orig = 'ABCDEFGHIJKLM'
     tgt = 'NOPQRSTUVWXYZ'
     rotmapper = dict(zip(orig + tgt, tgt + orig))
     resultado = ''.join(rotmapper.get(x.upper(), x) for x in palabra)

     return resultado.lower()


           