def validar_expresion(expresion):
    lista=list(expresion)
    if len(lista)==3:
        a=lista[0]
        b=lista[1]
        c=lista[2]
        if a.isdigit() and (b=="+" or b=="-") and c.isdigit():
            return True
        else:
            return False
    if len(lista)<3:
        return False
    

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))