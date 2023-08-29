def validar_expresion(expresion):
    if expresion.find("+")==-1 and expresion.find("-")==-1:
        return True
    if expresion.find("+")!=0 and expresion.find("+")!=(len(expresion)-1) and expresion.find("+")!=-1:
        return validar_expresion(expresion[expresion.find("+")+1:])
    elif expresion.find("-")!=0 and expresion.find("-")!=(len(expresion)-1) and expresion.find("-")!=-1:
        return validar_expresion(expresion[expresion.find("-")+1:])
    else:
        return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           