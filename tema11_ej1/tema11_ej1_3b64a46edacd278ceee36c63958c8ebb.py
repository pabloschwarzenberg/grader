def palindromo(palabra,arbalap="",i=-1):
    if(len(palabra) == len(arbalap)):
      return arbalap == palabra
    return palindromo(palabra,arbalap + palabra[i],i-1)

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           