def validar_expresion(expresion):
    lista=list(expresion)
    if len(lista)==2:
        return False
    i=0
    while i<len(lista)-1:
        if lista[i]==lista[i+1]:
            return False
        i+=1

    return True

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           