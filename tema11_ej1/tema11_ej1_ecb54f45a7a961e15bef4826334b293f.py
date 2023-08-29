def palindromo(palabra):
    l = list(palabra)
    l.reverse()
    b ="".join(l)
    if palabra == b:
      return True
    return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           