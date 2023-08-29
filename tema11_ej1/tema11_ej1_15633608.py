def palindromo(palabra):
    if len(palabra) == 1:
        return True
    else:
        a = False
        if palabra[0] == palabra[len(palabra)-1]:
            b=list(palabra)
            b.pop(0)
            b.pop(len(b)-1)
            a = palindromo("".join(b))
        return a

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           