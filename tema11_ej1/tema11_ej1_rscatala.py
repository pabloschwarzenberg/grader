def palindromo(palabra):
    caracteres = list(palabra)
    if len(caracteres) == 1:
        return True
    if caracteres[0] == caracteres[-1]:
        del caracteres[0]
        del caracteres[-1]
        "".join(caracteres)
        return palindromo(caracteres)
        
    return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           