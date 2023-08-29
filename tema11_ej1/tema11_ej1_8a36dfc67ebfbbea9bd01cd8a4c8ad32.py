def palindromo(palabra):
    if palabra[0]==palabra[len(palabra)-1]:
      return True
    else:
      return False

    return

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           