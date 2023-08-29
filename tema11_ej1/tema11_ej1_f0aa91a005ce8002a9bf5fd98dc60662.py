def palindromo(palabra):
    palabra_a_leer = list(palabra)
    palabra_a_leer.reverse()
    palabra2 = "".join(palabra_a_leer)
    if palabra == palabra2:
     return True
    else :
      print(palabra_a_leer)
      return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           