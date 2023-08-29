def rot13(palabra):
  abecedario = "abcdefghijklmnopqrstuvwxyz"
  trans = abecedario[13:] + abecedario[:13]
  rot_abecedario = lambda c: trans[abecedario.find(c)] if abecedario.find(c)>-1 else c
  return ''.join( rot_abecedario(c) for c in palabra )
  pass

if __name__=="__main__":
  palabra=input("Ingresa la palabra que quieras encriptar: ")
  palabra.lower()
  resultado=rot13(palabra)
  print("El resultado es: ",resultado)
           