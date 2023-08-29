def palindromo(palabra):
    largo=len(palabra)
    if largo<2:
        return True
    if palabra[0]!=palabra[-1]:
        return False
    else:
        return palindromo(palabra[1:largo-1])

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           