def palindromo(palabra):
    if len(palabra)==1:
      return True
    
    else:
      if palabra[0]==palabra[len(palabra)-1]:
         return palindromo(palabra[1:((len(palabra))-1)])
         
      else:
         return False
      


if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           