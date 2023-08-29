def palindromo(palabra):
    pal=list(palabra)
    pal.reverse()
    if pal==list(palabra):
     return True
    else:
     return False
 
 
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           