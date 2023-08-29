def palindromo(palabra):
    palabra=list(palabra)
    palabra1=[]
    for i in range(len(palabra)):
      palabra1.insert(0,palabra[i])
    if str(palabra1)==str(palabra):
      return True
    else:
      return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           