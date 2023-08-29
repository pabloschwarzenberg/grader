orig = 'abcdefghijklm'
camb = 'nopqrstuvwxyz'
def rot13(palabra):
  a = palabra.translate(palabra.maketrans(orig, camb))
  print(a) 