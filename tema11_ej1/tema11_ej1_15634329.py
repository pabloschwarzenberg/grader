def palindromo(palabra):
    if len(palabra)==1 or palabra=="":
      return True
    elif palabra[0]==palabra[len(palabra)-1]:
      p=palabra[1:len(palabra)-2]
      return palindromo(p)
    else:
      return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           