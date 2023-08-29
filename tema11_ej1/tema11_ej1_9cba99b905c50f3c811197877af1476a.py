def palindromo(palabra):
    if len(palabra) <=1:
        return True
    if palabra[0] == palabra [-1]: # secuencia[-1] es la ultima letra de la palabra
        return palindromo(palabra[1:-1]) #segund letra a la penultima
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           