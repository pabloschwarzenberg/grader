def palindromo(palabra):
    if palabra[0] == palabra[-1] and len(palabra) > 1:
      print(palabra)
      return palindromo(palabra[1:-1])
    else:
      return palabra[0] == palabra[-1]
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           