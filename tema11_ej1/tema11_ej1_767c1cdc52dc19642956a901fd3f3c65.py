def palindromo(palabra):
    x=palabra[::-1]
    if palabra==x:
        return True
    else:
        return False
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           