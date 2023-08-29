def palindromo(palabra):
  x = len(palabra)
  reflejo = []
  i=1
  while x-i >= 0:
    reflejo.append(palabra[x-i])
    i+=1

  reflejox = "".join(reflejo)
  if reflejox == palabra:
    return True
  else:
    return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           