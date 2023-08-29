def palindromo(palabra):
    palabra=list(palabra)
    palabra1=palabra[::-1]
    if palabra==palabra1:
      return True
    else:
      return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           