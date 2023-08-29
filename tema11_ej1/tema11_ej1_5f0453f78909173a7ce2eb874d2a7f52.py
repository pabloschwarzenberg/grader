def palindromo(palabra):
    return palabra == palabra[::-1]

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           