def palindromo(palabra):
    a=palabra[::-1]
    if a==palabra:
      return True
    else:
      return False
    return

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           