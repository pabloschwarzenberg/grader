def palindromo(palabra):
    if len(palabra)==1 or len(palabra)==0:
      return (True)
    if palabra[0]==palabra[len(palabra)-1]:
      palabra=palabra[1:len(palabra)-2]
      return(palindromo(palabra))
    else:
      return(False)
    return

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           