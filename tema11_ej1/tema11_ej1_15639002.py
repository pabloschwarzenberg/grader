def palindromo(palabra):
    palabra=palabra.split(" ")
    palabra="".join(palabra)
    resultado=comparar(palabra)
    
    if resultado:
      return True
    else:
      return False

def comparar(palabra):
  if len(palabra)==0:
    return True
  else:
    if palabra[0]==palabra[len(palabra)-1]:
      return comparar(palabra[1:len(palabra)-1])
    else:
      return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           