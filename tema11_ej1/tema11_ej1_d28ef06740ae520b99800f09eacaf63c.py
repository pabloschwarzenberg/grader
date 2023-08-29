def palindromo2(palabra):
    n = 0
    k = len(palabra)-1
    while n<len(palabra):
      if palabra[n] == palabra[k-n]:
        n = n + 1
      else:
        return False
    return True

def palindromo(palabra):        
  last = len(palabra)-1
  if (last>2 and palabra[0] == palabra[last]):
    palabra.pop[0]
    palabra.pop[last-1]
    palindromo(palabra)
  elif (last<=2 and palabra[0] == palabra[last]):
    return True
  else:
    return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           