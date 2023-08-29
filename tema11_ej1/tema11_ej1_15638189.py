def palindromo(palabra):
    i=0
    l=len(palabra)
    if palabra[i]==palabra[l-(i+1)]:
        i+=1
        if i==(l//2):
          return True
        palindromo(palabra)
    return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           