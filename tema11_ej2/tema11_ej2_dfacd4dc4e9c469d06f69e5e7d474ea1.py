def validar_expresion(expresion):
    expresion = list(expresion)
    for i in expresion:
        if i not in ['0','1','2','3','4','5','6','7','8','9']:
            if expresion.index(i)+1 == len(expresion):
                return False
            elif expresion[expresion.index(i)+1] not in ['0','1','2','3','4','5','6','7','8','9']:
                return False
            else:
                return True

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           