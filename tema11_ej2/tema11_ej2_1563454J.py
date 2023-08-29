def validar_expresion(expresion):
    expresion_lista=list(expresion)
    if len(expresion_lista)<3:
        return False
    if expresion_lista[0]=='+' or expresion_lista[0]=='-':
        return False
    else:
        if (expresion_lista[1]=='+' or expresion_lista[1]=='-') and (expresion_lista[2]=='+' or expresion_lista[2]=='-'):
            return False
        else:
            return True

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           