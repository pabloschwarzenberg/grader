def palindromo(palabra):
    lista=list(palabra)
    lista2=list(palabra)
    lista2.reverse()
    if lista2==lista:
      return True
    else:
      return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))

           