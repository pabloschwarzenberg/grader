def validar_expresion(expresion):
    if "+" in expresion:
        e=expresion.split("+")
        print(e)
        if e[0] !="" and e[1] !="":
            return True
        else:
            return False
        
    if "-" in expresion:
        e=expresion.split("-")
        print(e)
        if e[0] !="" and e[1] !="":
            return True
        else:
            return False
    else:
        return False
    

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))