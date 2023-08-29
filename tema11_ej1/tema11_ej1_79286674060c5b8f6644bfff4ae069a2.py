def palindromo(palabra):
    reversa=palabra[::-1]
    if palabra==reversa:
      return True
    else:
      return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           