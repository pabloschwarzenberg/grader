def palindromo(palabra):
    if len(palabra)==0:
        return True
    if len(palabra)==1:
        print(palabra)
        return True
    if (len(palabra)>=2) and palabra[0]==palabra[-1]:
        palabra=palabra[1:-1]
        print(palabra)
        return palindromo(palabra)
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           