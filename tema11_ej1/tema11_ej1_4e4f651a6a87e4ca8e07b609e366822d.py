def palindromo(palabra):
    a=list(palabra)
    b=list(palabra)
    b.reverse()
    if a==b:
        return True
    if a!=b:
        return False

           


if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           