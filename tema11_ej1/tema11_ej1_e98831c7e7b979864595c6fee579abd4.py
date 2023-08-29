def palindromo(palabra):
  if len(palabra)==1:
    return True
  if len(palabra)==2 and palabra[0]==palabra[1]:
    return True
  else:
    if palabra[0]==palabra[len(palabra)-1]:
       palabra=palabra[1:len(palabra)-1]
       if palindromo(palabra):
         return True
    else:
      return False
  

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           