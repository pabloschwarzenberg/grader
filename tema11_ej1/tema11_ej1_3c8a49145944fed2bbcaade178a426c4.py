def palindromo(palabra):
    sin=""
    for letra in palabra:
        if letra!=" ":
            sin+= letra
    if len(sin)<=1:
        return True
    if sin[0]==sin[len(sin)-1]:
        return palindromo(sin[1:len(sin)-1])
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           