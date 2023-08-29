def validar_expresion(expresion):
    lista=[]
    if expresion!="":
        lista.append(expresion[:1])
        return validar_expresion(expresion[1:])
    if len(expresion)==0:
        if lista[1]=="+" or lista[1]=="-":
            if lista[0]=="2":
                if lista[-1]=="2" or lista[-1]=="3":
                    return True
    return False

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))
           