def palindromo(palabra):
  palabra = list(palabra)
  palabra = palabra[::-1]
  if palindromo(palabra) == palabra:
    return True
  else:
    return False
  

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           