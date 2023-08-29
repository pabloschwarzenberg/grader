def palindromo(palabra):
    for i in range(len(palabra)):
        if palabra[i-1] != palabra[-i]:
            return False
    else:
        return True
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           