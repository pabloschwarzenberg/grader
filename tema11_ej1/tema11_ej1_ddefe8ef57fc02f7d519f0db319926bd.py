def palindromo(palabra):
    l = len(palabra) // 2
    if l == 1:
        if palabra[0] == palabra[-1]:
            return True
        else:
            return False
    if palabra[0] == palabra[-1]:
        return palindromo(palabra[1:-1])
    else:
        return False
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           