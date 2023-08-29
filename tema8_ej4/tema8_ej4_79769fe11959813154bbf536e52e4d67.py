def rot13(palabra):

  alfa = "abcdefghijklmnopqrstuvwxyz"
  cod_secret = "".join([alfa[(alfa.find(c)+13)%26] for c in palabra])
  return cod_secret

           