def palindromo(palabra):
   palabra = palabra.replace(" ", "")
   if (len(palabra) == 1):
      return True
   if (palabra[0] != palabra[len(palabra)-1]):
      return False
   return palindromo(palabra[1:len(palabra)-1])

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
          