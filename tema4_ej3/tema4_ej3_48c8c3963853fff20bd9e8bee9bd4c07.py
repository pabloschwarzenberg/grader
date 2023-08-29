def jerigonzo(palabra):
  lista=list(palabra)
  i=0
  while i<len(palabra):
    if ord(lista[i])==ord("a"):
      lista[i]=lista[i]+"p"+"a"
    elif ord(lista[i])==ord("e"):
      lista[i]=lista[i]+"p"+"e"
    elif ord(lista[i])==ord("i"):
      lista[i]=lista[i]+"p"+"i"
    elif ord(lista[i])==ord("o"):
      lista[i]=lista[i]+"p"+"o"
    elif ord(lista[i])==ord("u"):
      lista[i]=lista[i]+"p"+"u"
    i=i+1
  r="".join(lista)
  return r

if __name__ == "__main__":
  p=input("Ingrese palabra: ")
  print(jerigonzo(p))         