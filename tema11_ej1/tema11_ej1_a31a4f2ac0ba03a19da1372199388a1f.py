def palindromo(palabra):
  derecha = palabra
  izquierda = palabra[::-1]
  if derecha == izquierda:
    return True
  else:
    return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           