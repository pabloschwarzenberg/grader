def palindromo(palabra):
    if len(palabra)==1 or len(palabra)==0:
       return True
    else:
        if palabra[0]==palabra[-1]:
            p0=palabra.lstrip(palabra[0])
            p1=p0.rstrip(palabra[-1])
            palabra_actual=palindromo(p1)
            return palabra_actual
        else:
            return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           