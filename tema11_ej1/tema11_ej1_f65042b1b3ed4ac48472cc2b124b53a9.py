def palindromo(palabra):
    if palabra==palabra[::-1]:
      return True
    return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           