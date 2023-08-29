def palindromo(palabra):
  palabra=list(palabra)
  if len(palabra)==0 or len(palabra)==1:
    return
  else:
    if palabra[0]==palabra[-1]:
      palabra.pop(0)
      palabra.pop(-1)
      palindromo(palabra)
      return True
    else:
      return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           