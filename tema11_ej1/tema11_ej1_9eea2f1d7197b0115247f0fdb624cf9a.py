def palindromo(palabra):
    palabra_o = palabra
    palabra1 = list(palabra_o)
    palabra1.reverse()
    palabra2 = "".join(palabra1)
    if palabra_o == palabra2:
        return True
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
