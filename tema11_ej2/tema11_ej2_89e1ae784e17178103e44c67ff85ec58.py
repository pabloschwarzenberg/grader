def validar_expresion(expresion):
    if (len(expresion)==1 and expresion[0].isdigit()):
        return True
    else:
        return  expresion!= "" and (expresion[0:2]!="--" and expresion[0:2]!="++") and  validar_expresion(expresion[1:len(expresion)])

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           