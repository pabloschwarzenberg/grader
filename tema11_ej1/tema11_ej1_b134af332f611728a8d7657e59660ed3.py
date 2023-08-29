def palindromo(palabra):
    a = palabra
    if len(palabra) == 1 or len(palabra) == 0:
      return True
    if a[0] == a[-1]:
      return palindromo(palabra[1:-1])
    else:
      return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           