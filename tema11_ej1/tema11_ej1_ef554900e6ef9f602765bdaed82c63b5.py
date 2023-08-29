def palindromo(palabra):
    palabra_rev = list(palabra)
    palabra = "".join(palabra)
    palabra_rev.reverse()
    palabra_rev = "".join(palabra_rev)
    if palabra_rev == palabra:
      return True
    else:
      return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           