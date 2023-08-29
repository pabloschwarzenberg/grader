def palindromo(palabra):
    if palabra=="".join(reversed(list(palabra))):
      return True
    else:
      return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           