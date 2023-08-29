def palindromo(palabra):
    if len(palabra)==0:
      return True
    elif len(palabra)==1:
      return True
    else:
      palabra=list(palabra)
      if palabra[0]==palabra[len(palabra)-1]:
        palabra.pop(0)
        palabra.pop(len(palabra)-1)
        palabra="".join(palabra)
        return palindromo(palabra)
      else:
        return False
    

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           