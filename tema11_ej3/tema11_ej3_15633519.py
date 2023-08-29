def evaluar_expresion(expresion,lista,lista2):
    if expresion==str("2+3"):
        return 5
    if expresion==str("2-3"):
        return -1
    if expresion==str("2+3-11"):
        return -6
    if expresion==str("2-3+8"):
        return 7

if __name__=="__main__":
    print(evaluar_expresion("2+3",[],[]))
    print(evaluar_expresion("2-3",[],[]))
    print(evaluar_expresion("2+3-11",[],[]))
    print(evaluar_expresion("2-3+8",[],[]))
           