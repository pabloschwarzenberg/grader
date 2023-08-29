def palindromo(palabra):
    if len(palabra)==0 or len(palabra)==1:
      return True
    if palabra[0]==palabra[-1]:
       a=palabra[1:-1]
       return palindromo(a)
    elif palabra[0]!=palabra[-1]:
      return False
    

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           