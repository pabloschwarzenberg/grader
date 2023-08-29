def palindromo(palabra):
    if palabra[::-1]==palabra:
        return True
    return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           