def palindromo(palabra):
    if len(palabra)==1:
      return True
    if len(palabra)==2:
      return True
    else:
      cabeza = palabra[0]
      cuerpo = palabra[1:len(palabra)-1]
      ultima = palabra[-1]
      if palindromo(cuerpo)==True and cabeza==ultima:
        return True
      else:
        return False
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           