def validar_expresion(expresion):
    if expresion[0]=="-" or expresion[0]=="+" or expresion[len(expresion)-1]=="-" or expresion[len(expresion)-1]=="+":
        return False
    if expresion=="+" or expresion=="-":
        return False
    if expresion.find("+")!=-1:
        a=list(expresion)
        a.remove("+")
        u="".join(a)
        return validar_expresion(u)
    if expresion.find("-")!=-1:
        a=list(expresion)
        a.remove("-")
        u="".join(a)
        return validar_expresion(u)
    return True
    
if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           