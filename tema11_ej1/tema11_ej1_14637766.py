def palindromo(palabra):
    if len(s)<1:
      return True
    else: 
      if s[0]==s[-1]:
        return palindromo(se[1:-1])
      else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           