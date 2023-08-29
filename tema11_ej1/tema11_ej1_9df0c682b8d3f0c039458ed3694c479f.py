def palindromo(palabra):
    s=palabra[0]
    if len(palabra)-1<=0:
      return True
    if palabra[len(palabra)-1]!=s:
      return False
    if palabra[len(palabra)-1]==s:
      d=palabra[1:len(palabra)-1]
      palindromo(d)
    return palindromo(d)

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           