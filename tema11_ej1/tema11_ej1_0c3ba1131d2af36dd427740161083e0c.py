def palindromo(palabra):
    palabra2=list(palabra)
    palabra3=list(reversed(palabra2))
    if palabra2==palabra3:
           return True
    else:
           return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           