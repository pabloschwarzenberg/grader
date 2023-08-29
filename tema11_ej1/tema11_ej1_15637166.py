def palindromo(palabra):
    palabra_invertida = palabra[::-1]
    if palabra_invertida==palabra:
        return True
    else:
        return False
        

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           