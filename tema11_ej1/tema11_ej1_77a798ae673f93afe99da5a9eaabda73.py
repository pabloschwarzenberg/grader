def revertir(palabra):
    return palabra[::-1]
 
def palindromo(palabra):
    reversa = revertir(palabra)
    if (palabra == reversa):
        return True
    return False
 
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           