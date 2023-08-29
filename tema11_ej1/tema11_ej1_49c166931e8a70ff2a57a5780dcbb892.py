def palindromo(palabra):
   l=list(reversed(palabra))
   l="".join(l)
   if palabra==l:
      return True
   else:
      return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           