def palindromo(palabra):
    if len(palabra)<=1:
        return True
    else:
        if palabra[-1]==palabra[0]:
            palabra=list(palabra)
            palabra.pop(0)
            palabra.pop(-1)
            palabra="".join(palabra)
            return palindromo(palabra)
        else:
            return False
        
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))