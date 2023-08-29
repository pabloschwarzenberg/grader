def validar_expresion(expresion):
    ex=list(expresion)
    en=ex.count("0")+ex.count("1")+ex.count("2")+ex.count("3")+ex.count("4")+ex.count("5")+ex.count("6")+ex.count("7")+ex.count("8")+ex.count("9")
    em1=expresion.count("+")
    em2=expresion.count("-")
    if en>(em1+em2):
        return True
    elif en<=(em1+em2):
        return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           