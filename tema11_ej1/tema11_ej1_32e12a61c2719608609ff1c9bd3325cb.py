def palindromo(palabra):
    sal=palabra[::-1]
    
    if sal==palabra:
      return True
    else:
      return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           