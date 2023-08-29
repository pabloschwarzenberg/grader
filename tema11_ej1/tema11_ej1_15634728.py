def palindromo(palabra):
    if palabra[0] == palabra[-1]:
        if len(palabra) == 2 or len(palabra) == 1:
            return True
        return palindromo(palabra[1:-1])
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           
