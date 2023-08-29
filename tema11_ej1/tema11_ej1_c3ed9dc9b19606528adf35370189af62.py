def palindromo(palabra):
    palabra=list(palabra)
    palabra2=list(palabra)
    palabra2.reverse()
    if palabra==palabra2:
      return True
    else:
      return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           