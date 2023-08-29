def palindromo(palabra):
    palabra=palabra.strip()
    a=list(palabra)
    b=list(palabra)
    b.reverse()
    if a==b:
        return True
    else:
        return False
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           