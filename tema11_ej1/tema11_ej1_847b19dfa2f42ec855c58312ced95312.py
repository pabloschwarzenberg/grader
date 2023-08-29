def palindromo(palabra):
    cadena =(palabra)
    if len(cadena)<2:
        return True
    if (cadena[0] != cadena[-1]):
        return False
    if cadena[0]== cadena[-1]:
        cadena=cadena[1:-1]
        return palindromo(cadena)


if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           