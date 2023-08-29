def palindromo(palabra):
    if len(palabra)<=1:
      return True
    
    
    else:
       while i<len(palabra)/2:  
         if palabra[i]==palabra[-i]:
           return palindromo(palabra.pop(palabra[i],palabra[-i])

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           