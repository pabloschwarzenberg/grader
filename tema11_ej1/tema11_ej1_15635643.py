def palindromo(frase): #OK
    frase=frase.strip()
    if len(frase)==1 or frase=="":
        return True
    elif frase[0]==frase[len(frase)-1]:
        new=frase[1:len(frase)-1]
        return palindromo(new)
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           