def palindromo(palabra,resultado=True):
    largo=len(palabra)
    if largo==0 or largo==1:
        return True
    elif palabra[0]!=palabra[-1]:
        return False
    elif palabra[0]==palabra[-1]:
        palabra=palabra[1:-1]
        return palindromo(palabra,resultado)
        
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))