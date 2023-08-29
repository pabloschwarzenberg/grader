def palindromo(palabra):
    palabra = palabra.lower()
    palabra = list(palabra)
    if len(palabra) == 0:
        return True
    else:
        if len(palabra) == 1:
            return True
        elif palabra[0] == palabra[-1]:
            palabra.pop[0]
            palabra.pop[-1]
            palindromo(palabra)
        else:
            return False
   
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           