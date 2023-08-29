def palindromo(palabra):
    if len(palabra)==1:
      return True
    if len(palabra)==2:
      return(palabra[0]==palabra[1])
    else:
      a=palabra[1:len(palabra)-1]
      b=palindromo(a)
      if b==True and palabra[0]==palabra[len(palabra)-1]:
        return True
      else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           