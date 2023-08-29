def palindromo(palabra):
  return palindromo2(palabra,len(palabra))
  
def palindromo2(palabra,l,x=0):
    if len(palabra)<=1:
        if x==l//2:
            return True
        else:
            return False
        

    if palabra[0]==palabra[len(palabra)-1]:
        return palindromo2(palabra[1:len(palabra)-1],l,x+1)        

    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           