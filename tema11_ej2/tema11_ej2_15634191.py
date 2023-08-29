def validar_expresion(expresion):
    op=["+","-"]
    loc=expresion.find("+")
    if loc==-1:
        loc=expresion.find("-")
        if loc==-1:
            return True
    if loc==0 or loc==(len(expresion)-1):
        return False
    elif (expresion[loc-1]).isdigit in op or (expresion[loc+1]).isdigit() in op:
        return False
    expresion=expresion.replace(expresion[loc],"",1)
    return validar_expresion(expresion)