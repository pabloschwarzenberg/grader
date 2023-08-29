def palindromo(palabra):
  if len(palabra)<2:
    return True
  if palabra[0]==palabra[-1]:
    palabra=palabra[1:-1]
    palindromo(palabra)
  else:
    return False 
  return True

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           