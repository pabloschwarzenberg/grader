def palindromo(palabra):
    for i in range(0,len(palabra)):
        if palabra[i]==palabra[-i-1]:
          return True
        else:
          return False
        

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           