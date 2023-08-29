def palindromo(palabra):
    if len(palabra)<=1:
      return True
    else:
      return palabra[0] == palabra[-1] and palindromo(palabra[1:-1])

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))

           