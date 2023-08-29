def rot13(p):
  abc = list("abcdefghijklm")
  nop = list("nopqrstuvwxyz")
  p = list(p)
  P = []
  i = 0
  while i < len(p):
    if p[i] in abc:
      A = abc.index(p[i])
      P.append(nop[A])
      i += 1
    else:
      N = nop.index(p[i])
      P.append(abc[N])
      i += 1
  return "".join(str(letra) for letra in P)

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           