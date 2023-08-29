def palindromo(palabra):
    if len(palabra)==1 or len(palabra)==0:
        return True
    elif palabra[-1]==palabra[0]:
        palabra=palabra.strip(palabra[0])
        return palindromo(palabra)
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           