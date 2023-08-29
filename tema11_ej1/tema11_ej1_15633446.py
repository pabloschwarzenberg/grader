def palindromo (palabra):
    if len(palabra)<=1:
        return True
    else:
        l=len(palabra)
        if palabra[0]==palabra[l-1]:
            palabra_corta=palabra[1:l-1]
            print(palabra_corta)
            palindromo(palabra_corta)
        else:
            return False
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           