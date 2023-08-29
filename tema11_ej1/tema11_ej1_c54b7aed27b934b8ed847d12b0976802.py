def palindromo(palabra):
    global pal
    if len(palabra)>1:
        pal=pal+palabra[-1]
        palindromo(palabra[0:len(palabra)-1])
    else:
        pal = pal + palabra[0]
        
    if len(pal)==len(palabra):
        if pal==palabra:
            pal=""
            return True
        else:
            pal = ""
            return False


pal=""
print(palindromo("oso"))
print(palindromo("dinosaurio"))

