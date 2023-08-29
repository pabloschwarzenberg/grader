def rot13(palabra):
  letras = "abcdefghijklmnopqrstuvwxyz"
  trans = letras[13:]+letras[:13]
  rot_let = lambda c: trans[letras.find(c)] if letras.find(c)>-1 else c
  return ''.join( rot_let(c) for c in palabra ) 
  pass
if __name__=="__main__":
  palabra = input("Ingresa la palabra que quieras encriptar: ")
  palabra.lower()
  resultado = rot13(palabra)
  print("El resultado es: ",resultado)
           