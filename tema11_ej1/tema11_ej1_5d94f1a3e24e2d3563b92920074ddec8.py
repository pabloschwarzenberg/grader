def palindromo(palabra,alrevez=[]):
    original=palabra.split(" ")
    if len(original)==1:
        alrevez.append(original[0])
        nueva="".join(alrevez)
        if nueva==palabra:
            return True
        else:
            return False
    x=original.pop()
    alrevez.append(x)
    seleccion(palabra)
        
        
    return

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           
