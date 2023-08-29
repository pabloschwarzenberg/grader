def palindromo(palabra):
  lista=list(palabra)
  lista2=lista[::-1]
  if lista2==lista:
    return True
  else:
    return False


if __name__ == "__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))

    
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           