def palindromo(palabra):
    a=list(palabra)
    if a == a[::-1]:
     return True
    else: 
      return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           