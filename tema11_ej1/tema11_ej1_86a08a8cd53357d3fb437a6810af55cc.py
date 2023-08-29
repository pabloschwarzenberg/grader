def palindromo(palabra):
    if len(palabra) == 0 or len(palabra) == 1:
        return True
    else:
        palabra = list(palabra)
        if palabra[0] == palabra[-1]:
            palabra.pop(0)
            palabra.pop(-1)
            return palindromo(palabra)
        else:
            return False
    

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           