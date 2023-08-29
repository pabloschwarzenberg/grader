def palindromo(palabra):
    if len(palabra)==1 or len(palabra)==0:
      return True
    elif len(palabra)>1 and palabra[0]==palabra[-1]:
      return palindromo(palabra[1:-1])
    else:
      return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           